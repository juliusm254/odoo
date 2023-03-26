from operations.models import Order, SafetyChecklist, SafetyChecklistQuestion, Labinspection, LabResultsDecision, Loading
from django.shortcuts import get_object_or_404

def order_status_update(order, order_status):
    order.order_status = order_status
    order.save()



def checklist_create(*,order_id:str, question_id:str, checklist_choice:str ,**kwargs) -> SafetyChecklist:    
    question_obj = get_object_or_404(SafetyChecklistQuestion, id=question_id)
    order_obj = get_object_or_404(Order, id=order_id)
    SafetyChecklist.objects.create(order=order_obj, checklist_choice=checklist_choice, question=question_obj)
    order_status_update(order_obj, 'LAB')

def lab_create(*,order_id:str, pressure:str, oxygen:str, methane:str ,**kwargs) -> Labinspection:
    order_obj = get_object_or_404(Order, id=order_id)
    Labinspection.objects.create(order=order_obj, pressure=pressure, oxygen=oxygen, methane=methane)
    order_status_update(order_obj, 'LABRESULTS')

def lab_results_create(*,order_id:str, order_status:str) -> LabResultsDecision:
    order_obj = get_object_or_404(Order, id=order_id)
    if order_status == 'VENT':      
        LabResultsDecision.objects.create(order=order_obj, vent=True)
    else:
        if order_status == 'SEAL':
            LabResultsDecision.objects.create(order=order_obj, seal=True)
        else:
            LabResultsDecision.objects.create(order=order_obj)
    order_status_update(order_obj, order_status)

def loading_create(*,order_id:str, net_weight:str, tare_weight:str, gross_weight:str) -> Loading:
    order_obj = get_object_or_404(Order, id=order_id)
    Loading.objects.create(order=order_obj, net_weight=net_weight, tare_weight=tare_weight, gross_weight=gross_weight)
    order_status_update(order_obj, 'LOADED')
        


# def perform_create(self, serializer):
#         print(self.request.data)
#         order = get_object_or_404(Order, id=self.request.data['order'])
#         update_order = order_status_update(order, self.request.data['status'])
#         return Response(status=202)