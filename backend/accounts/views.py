from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

#Signin은 Json에 의해 처리되므로 필요없다

class SingupView(APIView):
    permission_classes = (permissions.AllowAny, )


    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error' : '이메일이 이미 존재합니다.'})
            else:
                if len(password) < 6:
                    return Response({'error' : '비밀번호는 최소 6글자 이상이여야 합니다.'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name )
                    user.save()
                    return Response({'success' : '성공적으로 가입되었습니다.'})


        else:
            return Response({'error' : '패스워드가 맞지 않습니다.'})
