from django.shortcuts import get_object_or_404
from django.http import HttpResponse, FileResponse
from datetime import datetime

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import SafetyChecklist
# from customers.serializers import OrderSerializer
from .services import checklist_create, lab_create, loading_create, lab_results_create
from .selectors import order_list, checklist_details, labinspection_details, checklist_details_list, get_order
from .utils import create_pdf
from .serializers import VehicleSerializer,OrderSerializer, SafetyChecklistQuestionSerializer
import xmlrpc.client
from odooapi.sales_order_xmlrpc import LibraryAPI

class ChecklistCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        order_id = serializers.CharField()
        question_id = serializers.IntegerField()
        checklist_choice = serializers.CharField()

    def post(self, request):
        # que = []
        # choices = []
        order = self.request.data['order']
        questions = self.request.data['questions']
        for index in range(len(questions)):
            question_list=list(questions[index].values())
            # print(question_list)
            checklist_choice = question_list[2]
            # print(checklist_choice)
            question = question_list[0]
            # que.append(question)
            # choices.append(checklist_choice)
            # print(choices)
            # print(que)
            serializer = self.InputSerializer(data={'order_id':order, 'question_id':question, 'checklist_choice':checklist_choice})
            serializer.is_valid(raise_exception=True)

            checklist_create(**serializer.validated_data)



        return Response(status=status.HTTP_201_CREATED)


class ChecklistListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(order_list('SAFETY'), many=True)
        print(serializer.data)
        return Response(serializer.data)

class ChecklistDetailAPI(APIView):
    
    # class OutputSerializer(serializers.ModelSerializer):        
    #     class Meta:
    #         model = SafetyChecklist
    #         fields = ['question','checklist_choice', 'created_at']
    #         depth = 2
    
    class OutputSerializer(serializers.Serializer):
        # id = serializers.IntegerField()        
        trailer_details = OrderSerializer(source="order", read_only=True)
        truck_details = OrderSerializer(source="order", read_only=True)
        question_desc = SafetyChecklistQuestionSerializer(source="question", read_only=True)
        order_id = serializers.IntegerField()
        checklist_choice = serializers.CharField()
        
    def get(self, request, pk=None):
        serializer = self.OutputSerializer(checklist_details(pk), many=True)
        # print(serializer.data)
        print(serializer.data[0]["checklist_choice"])
        print(serializer.data[1]["checklist_choice"])
        # contract = Contract.query.get(id)
        # contractor = SafetyChecklist.objects.get(contract.contractor_id)
        # booking = Booking.query.filter_by(contract_id=contract.id).first()
        pdf = create_pdf(
                            # booking_no=pk,
                            order_no=pk,
                            # contractor=serializer.data[0]['trailer_details']['trailer_details']['registration'],
                            truck_reg=serializer.data[0]['truck_details']['truck_details']['registration'],
                            truck_epra=serializer.data[0]['truck_details']['truck_details']['epra_no'],
                            truck_trans=serializer.data[0]['truck_details']['truck_details']['transporter'],                            
                            trailer_reg=serializer.data[0]['trailer_details']['trailer_details']['registration'],
                            trailer_epra=serializer.data[0]['trailer_details']['trailer_details']['epra_no'],
                            trailer_trans=serializer.data[0]['truck_details']['truck_details']['transporter'],
                            # Questions

                            q1=serializer.data[0]["question_desc"]['question_desc'],
                            q2=serializer.data[1]["question_desc"]['question_desc'],
                            q3=serializer.data[2]["question_desc"]['question_desc'],
                            q4=serializer.data[3]["question_desc"]['question_desc'],
                            c1=serializer.data[0]["checklist_choice"],
                            c2=serializer.data[1]["checklist_choice"],
                            c3=serializer.data[2]["checklist_choice"],
                            c4=serializer.data[3]["checklist_choice"],


                            warehouse="contract.warehouse",
                            date=10/5/2022,
                            time=datetime.now(),
                            pallets_pos="pallets_position",
                            pallets="pallets_actual"
                            )
        pdf.seek(0)
        
        response = HttpResponse(pdf, headers={
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'attachment; filename="foo.pdf"',
        })
        return(response)
        return Response(serializer.data)


# class ChecklistDetailAPI(APIView):
    
#     class OutputSerializer(serializers.ModelSerializer):        
#         class Meta:
#             model = SafetyChecklist
#             fields = ['question','checklist_choice', 'created_at']
#             depth = 1


#     def get(self, request, pk=None):
#         serializer = self.OutputSerializer(checklist_details(pk), many=True)
#         print(serializer.data)
#         return Response(serializer.data)

# class ChecklistDetailApi(APIView):
#     def get(self, request, pk=None):
        

#         data = get_checklist_details(pk)

#         return Response(data)


class PrintSafetyListAPI(APIView):    
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(checklist_details_list(), many=True)
        # serializer = SafetyChecklist.objects.filter().select_related().all()
        # print(serializer.data)
        return Response(serializer.data)


class LabInspectionListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)


    def get(self, request):
        serializer = self.OutputSerializer(order_list('LAB'), many=True)
        print(serializer.data)
        return Response(serializer.data)

class LabInspectionCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        pressure = serializers.IntegerField()
        oxygen = serializers.IntegerField()
        methane = serializers.IntegerField()
        nitrogen = serializers.IntegerField()
        order_id = serializers.IntegerField()

    def post(self, request):
        order = self.request.data['order']
        pressure = self.request.data['truck_pressure']
        oxygen = self.request.data['oxygen_content']
        nitrogen = self.request.data['nitrogen_content']
        methane = self.request.data['methane_content'] 
        serializer = self.InputSerializer(data={'order_id':order, 
                                                'pressure':pressure, 
                                                'oxygen':oxygen, 
                                                'methane':methane, 
                                                'nitrogen':nitrogen})
        serializer.is_valid(raise_exception=True)
        lab_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class LabResultsListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('LABRESULTS'), many=True)
        return Response(serializer.data)

class LabResultsCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        order_status = serializers.CharField()        
        order_id = serializers.IntegerField()

    def post(self, serializer):
        order = self.request.data['order']
        order_status = self.request.data['status']
        serializer = self.InputSerializer(data={'order_id':order, 'order_status':order_status})
        serializer.is_valid(raise_exception=True)
        lab_results_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

class LabInspectionDetailsAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        pressure = serializers.IntegerField()
        oxygen = serializers.IntegerField()
        methane = serializers.IntegerField()
        order_id = serializers.IntegerField()

    def get(self, serializer, pk=None):
        serializer = self.OutputSerializer(labinspection_details(pk), many=True)
        return Response(serializer.data)


class LabSealListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('SEAL'), many=True)
        return Response(serializer.data)

class LabVentListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('VENT'), many=True)
        return Response(serializer.data)

class LoadingListAPI(APIView):
    permission_classes = [IsAuthenticated,]
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        trailer_details = VehicleSerializer(source="trailer", read_only=True)
        truck_details = VehicleSerializer(source="truck", read_only=True)

    def get(self, request):
        serializer = self.OutputSerializer(order_list('LOADING'), many=True)
        return Response(serializer.data)

class LoadingCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):                
        order_id = serializers.IntegerField()
        net_weight = serializers.IntegerField()
        tare_weight = serializers.IntegerField()
        gross_weight = serializers.IntegerField()

        

    def post(self, serializer):
        order = self.request.data['order']
        net_weight = self.request.data['net_weight']
        tare_weight = self.request.data['tare_weight']
        gross_weight = self.request.data['gross_weight']    
        serializer = self.InputSerializer(data={'order_id':order, 'net_weight':net_weight, 'tare_weight':tare_weight, 'gross_weight':gross_weight})
        serializer.is_valid(raise_exception=True)
        loading_create(**serializer.validated_data)
        odoo_api = LibraryAPI( host='172.23.0.3', 
                                port=8069, 
                                db='devel', 
                                user='admin', 
                                pwd='admin')

        print("we here")
        odoo_api._execute('create_sales_order', 'sale.order', [{
            'partner_id': 1677, # Replace with the customer's ID
            'so_name': order,
            'order_line': [(0, 0, {
                'product_id': 	2, # Replace with the product's ID
                'product_uom_qty': 1,
                'price_unit': 10.0, # Replace with the product's unit price                
                'name': "Order Line Name",
                'customer_lead': 0,
                'order_id': order
            })],
        }])
        return Response(status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     # Initialize Odoo API
    #     # host, port, db = "localhost", int(15069), "devel" 
    #     # user, pwd = "admin", "admin"
    #     # print(port)
    #     odoo_api = LibraryAPI( host='172.23.0.3', 
    #                             port=8069, 
    #                             db='devel', 
    #                             user='admin', 
    #                             pwd='admin')

    #     print("we here")

    #     # Parse input data
    #     serializer = self.InputSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     order_id = serializer.validated_data['order_id']
    #     net_weight = serializer.validated_data['net_weight']
    #     tare_weight = serializer.validated_data['tare_weight']
    #     gross_weight = serializer.validated_data['gross_weight']

    #     # Create sales order in Odoo
    #     odoo_api._execute('sale.order', 'create', [{
    #         'partner_id': 1, # Replace with the customer's ID
    #         'order_line': [(0, 0, {
    #             'product_id': 1, # Replace with the product's ID
    #             'product_uom_qty': 1,
    #             'price_unit': 10.0, # Replace with the product's unit price
    #         })],
    #     }])

    #     return Response(status=status.HTTP_201_CREATED)


