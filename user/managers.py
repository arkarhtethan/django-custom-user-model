# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):

# 	user_in_migration = True

# 	def _create_user(self, email, password, **kwargs):

# 		if not email:

# 			raise ValueError("Email must provide")

# 		email = self.normalize_email(email)

# 		user = self.model(email=email,**kwargs)

# 		user.set_password(password)

# 		user.is_staff=True

# 		return user

# 	def create_user(self, email, password, **kwargs):

# 		kwargs.setdefault('is_superuser',False)

# 		user = self._create_user(email, password, **kwargs)
	
# 	def create_superuser(self, email, password, **kwargs):

# 		kwargs.setdefault('is_superuser',True)

# 		user = self._create_user(email, password, **kwargs)

	


from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

	use_in_migration = True

	def _create_user(self, email, password, **kwargs):

		if not email:

			raise ValueError("Email must provided")

		email = self.normalize_email(email)

		user = self.model(email=email,**kwargs)
		
		user.is_staff = True

		user.set_password(password)

		user.save(using=self._db)

		return user

	def create_user(self, email, password, **kwargs):

		kwargs.setdefault('is_superuser',False)

		user = self._create_user(email, password, **kwargs)

	def create_superuser(self, email, password, **kwargs):

		kwargs.setdefault('is_superuser',True)

		if kwargs.get('is_superuser') is not True:

			raise ValueError("super user must have is_superuser=True")

		return self._create_user(email, password, **kwargs)

