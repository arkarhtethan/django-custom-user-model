from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(unique=True)

	first_name = models.CharField(max_length=120)

	last_name = models.CharField(max_length=120)

	is_active = models.BooleanField(default=True)

	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = []

	def get_full_name(self):

		return f'{self.first_name} {self.last_name}'

	def get_short_name(self):

		return self.first_name

	def __str__(self):

		return self.email