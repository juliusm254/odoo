from django.db.models.query import QuerySet
from customers.models import Customer


def customer_list() -> QuerySet[Customer]:    
    return(Customer.objects.objects.all())