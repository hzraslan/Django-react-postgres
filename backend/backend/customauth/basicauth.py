from django.db import models

class BasicCustomBackend(object):

        # Create an authentication method
    def authenticate(self, username, password):
        print('here;')
        try:
            # Try to find a user matching the username provided
            user = User.objects.get(username=username) 

            # if successful return user if not return None
            if password == user.password:
                return user
            else:
                return None
        except User.DoesNotExist:
            # No user was found
            return None

        # Required for the backend to work properly
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None