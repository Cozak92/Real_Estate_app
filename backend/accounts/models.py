from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    """일반 유저, 슈퍼유저 등을 만듬"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("이메일을 입력해야 합니다.")

        email = self.normalize_email(email)
        user = self.model(email = email, name=name)
 
        user.set_password(password) #패스워드 해싱하기 위한 함수
        user.save()

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user



class UserAccount(AbstractBaseUser, PermissionsMixin):
    """유저를 위한 모델"""
    email = models.EmailField(max_length = 255, unique= True) #메일로 유저를 구별하기위해서 유니크 지정
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default =True)
    is_staff = models.BooleanField(default = False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email