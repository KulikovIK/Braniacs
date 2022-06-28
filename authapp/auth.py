from django.contrib.auth.backends import ModelBackend
from authapp.models import User



class EmailAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        # loginmod = {'email': username} if '@' in username else {'username': username}

        try:
            # user = User.objects.get(**loginmod)
            if '@' in username:
                user = User.objects.get(email__iexact=username)
            else:
                user = User.objects.get(username__iexact=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id: int):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
