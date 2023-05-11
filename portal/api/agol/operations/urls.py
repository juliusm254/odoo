from django.urls import path
from operations.views import (LoginView, 
                    ScanOrder,                    
                    OrderDetailView,
                    SafetyCheckListQuestionCreateAPIView,
                    
                    )
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from operations.api import (
                    ChecklistCreateAPI, 
                    ChecklistListAPI, 
                    ChecklistDetailAPI, 
                    PrintSafetyListAPI, 
                    LabInspectionListAPI,
                    LabInspectionCreateAPI,
                    LabResultsCreateAPI,
                    LabResultsListAPI,
                    LabInspectionDetailsAPI,
                    LabSealListAPI,
                    LabVentListAPI,
                    LoadingCreateAPI,
                    LoadingListAPI
                    )


urlpatterns = [    
    
    path("login/", LoginView.as_view(), name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order_details"),
    path("scan-order/<int:pk>/", ScanOrder.as_view(), name="scan-order"),
    path('checklistcreate/', ChecklistCreateAPI.as_view(), name="check-list"),    
    path('checklist/', ChecklistListAPI.as_view(), name="check-list"),    
    # path('checklist/<int:pk>/', ChecklistDetailAPI.as_view(), name="detail-checklist"),
    path('checklist/<int:pk>/', ChecklistDetailAPI.as_view(),name="detail-checklist"),
    
    path('printsafety/', PrintSafetyListAPI.as_view(), name="safety-list"),
    path('checklist-questions/', SafetyCheckListQuestionCreateAPIView.as_view(), name="checklistquestions"),
    path('lab-inspection/', LabInspectionListAPI.as_view(), name="lab-inspection"),
    path('lab-create/',LabInspectionCreateAPI.as_view(), name="lab-create"),
    path('lab-results/',LabResultsListAPI.as_view(), name="lab-results"),
    path('lab-results-create/',LabResultsCreateAPI.as_view(), name="lab-results"),
    path('lab-results/<int:pk>/',LabInspectionDetailsAPI.as_view(), name="lab-results-details"),
    path('lab-seal/',LabSealListAPI.as_view(), name="lab-seal"),
    path('lab-vent/',LabVentListAPI.as_view(), name="lab-vent"),
    path('loading-list/',LoadingListAPI.as_view(), name="loading"),
    path('loading/',LoadingCreateAPI.as_view(), name="loading"),    
]