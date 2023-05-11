from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from operations.models import SafetyChecklistQuestion
from customers.models import Order, BulkOrder, Customer, Vehicle, CustomerTrailer, CustomerDriver, CustomerTruck, Driver
import random

class Command(BaseCommand):
    help="Command information"

    def handle(self, *args, **kwargs):
        
        fake = Faker()

        print("We are IN")

        print(fake.address())
        for _ in range(100):
            name =  fake.company()
            phone = random.randint(22155541, 554544541)
            email = fake.email()
            location = 'KSM'
            bulk_customer = random.randint(0, 1)
            Customer.objects.create(name=name, phone=phone, email=email, location=location, bulk_customer=bulk_customer)
            _ += 1
            print(f"Customer No {_}")

        for _ in range(300):
            registration = fake.license_plate()
            transporter = fake.company()
            epra_no = fake.license_plate()
            Vehicle.objects.create(registration=registration, transporter=transporter, epra_no=epra_no)
            _ += 1
            print(f"Vehicle No {_}")

        
        for _ in range(1):
            name = fake.name()
            national_id = random.randint(22155541, 554544541)
            epra_no = random.randint(2215, 554544)
            Driver.objects.create(name=name, national_id=national_id, epra_no=epra_no)
            _ += 1
            print(f"Driver No {_}")



        for _ in range(200):
            customer = Customer.objects.filter(pk=random.randint(1, 200)).first()    
            destination = 'KSM'    
            order_quantity = random.randint(25000, 30000)  
            
            driver = Driver.objects.filter(id=random.randint(1, 900)).first()    
            truck = Vehicle.objects.filter(id=random.randint(1, 400)).first()    
            trailer = Vehicle.objects.filter(id=random.randint(401, 600)).first()    
            Order.objects.create(customer=customer, destination=destination, order_quantity=order_quantity, driver=driver, truck=truck, trailer=trailer)
            _ += 1
            print(f"Order No {_}")


        
        # for _ in range(130):
        #     customer = Customer.objects.get(pk=random.randint(112, 113))
        #     quantity = random.randint(111, 112)
        #     BulkOrder.objects.create(customer=customer, quantity=quantity)
        #     _ += 1
        #     print(f"BulkOrder No {_} and IsBulk FLAG DOESNT DO Shit IF YOU See This")

        
        # for _ in range(4):
        #     question_desc = fake.sentence()
        #     SafetyChecklistQuestion.objects.create(question_desc=question_desc)
        #     _ += 1
        #     print(f"SafetyChecklistQuestion No {_}")


        for _ in range(20):
            customer = Customer.objects.get(pk=random.randint(1, 100))
            registration = fake.license_plate()
            trailer = Vehicle.objects.get(pk=random.randint(1, 300))
            CustomerTrailer.objects.create(registration=registration, customer=customer, trailer=trailer)
            _ += 1
            print(f"CustomerTrailer No {_}")


        for _ in range(50):
            customer = Customer.objects.get(pk=random.randint(1, 100))
            registration = fake.license_plate()
            truck = Vehicle.objects.get(pk=random.randint(1, 300))
            CustomerTruck.objects.create(registration=registration, customer=customer, truck=truck)
            _ += 1
            print(f"CustomerTruck No {_}")


        for _ in range(50):
            customer = Customer.objects.get(pk=1)
            name = fake.name()
            driver = Driver.objects.get(pk=random.randint(1, 200))
            CustomerDriver.objects.create(customer=customer, name=name, driver=driver)
            _ += 1
            print(f"CustomerDriver No {_}")


