from rest_framework import serializers
from rest_framework.views import APIView

from .selectors import customer_list

class CustomerListAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        odoo_customer_id = serializers.CharField()
        bulk_customer = serializers.CharField()

    def get(self, request):
        serializer = self.OutputSerializer(customer_list(), many=True)
        return Response(serializer.data)