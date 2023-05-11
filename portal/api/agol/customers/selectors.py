from django.db.models.query import QuerySet
from customers.models import Customer


def customer_list() -> QuerySet[Customer]:    
<<<<<<< Updated upstream
    return(Customer.objects.objects.all())
=======
    return(Customer.objects.all())
>>>>>>> Stashed changes
