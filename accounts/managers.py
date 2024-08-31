from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, full_name, date_of_birth, adress, national_code, phone, password=None):
        user = self.model(
            full_name=full_name,
            date_of_birth=date_of_birth,
            adress=adress,
            national_code=national_code,
            phone=phone,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, full_name, adress, national_code, phone, password=None):
        user = self.create_user(
            full_name=full_name,
            date_of_birth=None,
            adress=adress,
            national_code=national_code,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
