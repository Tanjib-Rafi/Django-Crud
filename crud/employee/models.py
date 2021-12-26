from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyAccountManager(BaseUserManager):
	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not name:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			name=name,
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			name=name,
		)
		user.is_active = True
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user



class Employee(AbstractBaseUser):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100,unique=True)
    GENDER_CHOICES = [
   ('Male', 'Male'),
   ('Female', 'Female')
    ]
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True)
    role_choice = [
    ('admin', 'admin'),
    ('employee', 'employee') 
    ]
    role = models.CharField(max_length=50,choices=role_choice,default="employee")
    is_active = models.BooleanField("IS_ACTIVE",default = True)
    created_at=models.DateField(auto_now_add=True, auto_now=False)
    updated_at=models.DateField(auto_now_add=False, auto_now=True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
     return self.email
    def has_perm(self, perm, obj=None):
     return self.is_superuser
    def has_module_perms(self, app_label):
     return True