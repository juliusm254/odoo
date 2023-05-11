from rest_framework import serializers
from customers.models import (BulkOrder, 
                    Order, 
                    Customer, 
                    Vehicle, 
                    Driver, 
                    CustomerDriver, 
                    CustomerTruck, 
                    CustomerTrailer)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        # fields = ['name', 'national_id']
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class CustomerTruckSerializer(serializers.ModelSerializer):
    truck_details = VehicleSerializer(source="truck", read_only=True)
    class Meta:
        model = CustomerTruck
        fields = ['truck','customer_id', 'truck_details', 'registration']

class CustomerTrailerSerializer(serializers.ModelSerializer):
    # trailer = VehicleSerializer()
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    class Meta:
        model = CustomerTrailer
        
        fields = ['trailer','customer_id', 'trailer_details', 'registration']


class CustomerDriverSerializer(serializers.ModelSerializer): 
    driver_details =  DriverSerializer(source="driver", read_only=True)
    class Meta:
        model = CustomerDriver
        fields = ['name', 'id', 'customer', 'driver_details']
        # fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    driver_details = DriverSerializer(source="driver", read_only=True)
    truck_details = VehicleSerializer(source="truck", read_only=True)
    trailer_details = VehicleSerializer(source="trailer", read_only=True)
    customer_details = CustomerSerializer(source="customer",  read_only=True)

    class Meta:
        
        model = Order
        fields = [
                    'id',
                    'driver',
                    'driver_details',
                    'trailer',
                    'trailer_details', 
                    'truck',
                    'truck_details', 
                    'created_at', 
                    'destination',
                    'order_quantity',
                    'order_status',
                    # 'customer',
                    'customer_details'
                ]
        
    
    def validate_order_quantity(self, value):
        if not value > 0:
            raise serializers.ValidationError('Quantity too Low')
        return value

                    
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class BulkOrderSerializer(serializers.ModelSerializer):
    # customer = serializers.StringRelatedField(many=False)
    class Meta:
        model = BulkOrder
        # fields = ['customer', 'quantity', 'description']
        fields = '__all__'