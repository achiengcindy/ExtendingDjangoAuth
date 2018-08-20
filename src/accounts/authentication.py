from django.contrib.auth.models import User

class EmailAuthBackend:
    # Email authentication
	def authenticate(self, username=None, password=None):
		try:
			user = CustomUser.objects.get(email=username)
			if user.check_password(password):
				return user
			return None
		except CustomUser.DoesNotExist:
			return None
	def get_user(self, user_id):
		try:
			return CustomUser.objects.get(pk=user_id)
		except CustomUser.DoesNotExist:
			return None
