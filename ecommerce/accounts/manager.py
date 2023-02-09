from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(phone_number=phone_number, email=BaseUserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password):
        user = self.create_user(phone_number, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
