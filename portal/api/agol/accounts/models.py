from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import transaction

from customers.models import Customer

# class UserManager(BaseUserManager):
#     def create_user(self, email, name, type, customer_id, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#     # def accelerate(self):
#     #     return "Go faster"
#         email = self.normalize_email(email)
#         email = email.lower()

#         user = self.model(
#             email= email,
#             customer_id = customer_id,
#             name=name
#         )

#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_operations_user(self, email, name, type, password=None):
#         user = self.create_user(email, name, password)

#         user.type = 'OPERATIONS'
#         user.save(using=self._db)

#         return user

#     def create_customer_user(self, email, name, type, customer_id, password=None):
#         user = self.create_user(email, name, type, customer_id, password)
#         user.type = 'CUSTOMER'
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, name, type, customer_id=None, password=None):
#         user = self.create_user(email, name, type, customer_id, password)
#         user.customer_id = None
#         user.is_superuser = True
#         user.is_staff = True
#         user.type = 'ADMIN'

#         user.save(using=self._db)

#         return user



# class User(AbstractBaseUser, PermissionsMixin):
    # OPERATIONS = 'OPERATIONS'
    # CUSTOMER = 'CUSTOMER'
    # ADMIN = 'ADMIN'

    # TYPE = (
    #     (OPERATIONS, 'Operations'),       
    #     (CUSTOMER, 'Customer'),
    #     (ADMIN, 'Admin'),
    #  )

    # email = models.EmailField(max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # type = models.CharField(max_length=25, choices=TYPE)
    # date_joined = models.DateTimeField(auto_now_add=True)

    # objects = UserManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name','type',]

    # def __str__(self):
    #     return self.email 


class UserManager(BaseUserManager):
    def create_user(self, email, name, customer_id, password=None, **extra_fields):
        try:
            if not email:
                raise ValueError('Users must have an email address')
            email = self.normalize_email(email)
            email = email.lower()

            defaults = {
                'name': name,
                'customer_id': customer_id,
                **extra_fields
            }
            user, created = self.get_or_create(email=email, defaults=defaults)

            if created:
                user.set_password(password)
                user.save(using=self._db)

            return user
        except Exception as e:
            # Log the error here or handle it in some other way
            raise e

    def create_operations_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('type', User.OPERATIONS)
        return self.create_user(email, name, password=password, **extra_fields)

    def create_customer_user(self, email, name, customer_id, password=None, **extra_fields):
        extra_fields.setdefault('type', User.CUSTOMER)
        return self.create_user(email, name, customer_id, password=password, **extra_fields)

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('type', User.ADMIN)
        extra_fields.setdefault('customer_id', None)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, name, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    OPERATIONS = 'OPERATIONS'
    CUSTOMER = 'CUSTOMER'
    ADMIN = 'ADMIN'

    TYPE_CHOICES = (
        (OPERATIONS, 'Operations'),
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
    )

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default=CUSTOMER)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def clean(self):
        # Check that customer_id is required for create_customer_user method
        if self._state.adding and self.type == self.CUSTOMER:
            if not self.customer_id:
                raise ValidationError('Customer ID is required for customer user')
