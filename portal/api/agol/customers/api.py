<<<<<<< Updated upstream
from rest_framework import serializers
from rest_framework.views import APIView

from .selectors import customer_list
=======
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import customer_list
from .services import customer_create
>>>>>>> Stashed changes

class CustomerListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        odoo_customer_id = serializers.CharField()
        bulk_customer = serializers.CharField()

    def get(self, request):
        serializer = self.OutputSerializer(customer_list(), many=True)
<<<<<<< Updated upstream
        return Response(serializer.data)
=======
        return Response(serializer.data)
    
class CustomerCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        odoo_customer_id = serializers.CharField()
        bulk_customer = serializers.CharField()
        phone = serializers.CharField()
        contact_person = serializers.CharField()
        email = serializers.EmailField()
        location = serializers.CharField()
        

    def post(self, request):
        print(self.request.data)
        name = self.request.data['name']
        odoo_customer_id = self.request.data['odoo_customer_id']
        bulk_customer = self.request.data['bulk_customer']
        phone = self.request.data['phone']
        email = self.request.data['email'] 
        contact_person = self.request.data['contact_person']
        location = self.request.data['location']  
        serializer = self.InputSerializer(data={'name':name, 
                                                'odoo_customer_id':odoo_customer_id, 
                                                'bulk_customer':bulk_customer, 
                                                'phone':phone, 
                                                'email':email,
                                                'contact_person':contact_person, 
                                                'location':location})
        serializer.is_valid(raise_exception=True)
        customer_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    
>>>>>>> Stashed changes
