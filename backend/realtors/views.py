from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerializer


# 1.데이터베이스에서 모든 중개업자들을 표시

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None

# 2. ID로 중개업자를 가져와서 표시
class RealtorView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    # list안에서 쓸꺼기때문에 퍼미션 있는지 체크안해도 된다
    # list로 반환 안할거기때문에 pagination_class 설정 안해줘도 된다
    serializer_class = RealtorSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtor.objects.filter(top_seller=True) #Topseller만 가져와서 표시
    serializer_class = RealtorSerializer
    pagination_class = None
    