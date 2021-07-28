from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

EXAMPLE_RECORD = {
    "username": "trung_cowell",
    "password": "12345678",
}


class CustomAuthen(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        login_valid = username == EXAMPLE_RECORD["username"]
        password_valid = password == EXAMPLE_RECORD["password"]
        if login_valid and password_valid:
            try:
                user = User.objects.get(username="trung")
                return user
            except User.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
