import json
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from operations.models import Order, SafetyChecklistQuestion
from rest_framework_simplejwt.tokens import RefreshToken
from operations.serializers import    (                          
                            ScanOrderSerializer, 
                            SafetyChecklistQuestionSerializer,                            
                            OrderSerializer
                            )
from django.contrib.auth import authenticate


def get_tokens_for_user(user):
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user' : user.id
    }


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request,):
        # type = request.POST['type']
        print(request.data)
        # if type == 'OPERATIONS':
        # username = request.data.get("username")
        # password = request.data.get("password")
        
        user = authenticate(username=request.data['username'], password=request.data['password'])
        # print(user + '2')
        if user.type=='OPERATIONS':
            return Response( get_tokens_for_user(user) )
        else:
            # return Response( get_tokens_for_user(user) )
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)




class OrderDetailView(APIView):
    serializer_class = OrderSerializer
    model = Order

    def get(self, request, pk=None):
        print(pk)
        queryset = Order.objects.get(id=pk)
        serializer = OrderSerializer(queryset)
        print(serializer.data)
        return Response(serializer.data)
    

class ScanOrder(generics.UpdateAPIView):
    permission_classes = ()

    def put(self, request, pk=None):
        data = json.loads(request.body.decode('utf-8'))
        instance = get_object_or_404(Order, id=pk)
        serializer = ScanOrderSerializer(instance, data=data)        
        if instance.order_status == 'PENDING':
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
        else:
            return Response(status=400)


class SafetyCheckListQuestionCreateAPIView(generics.ListCreateAPIView):    
    serializer_class = SafetyChecklistQuestionSerializer
    queryset = SafetyChecklistQuestion.objects.filter(active=True).order_by("id")


