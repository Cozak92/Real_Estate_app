from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    path('', RealtorListView.as_view()), 
    path('topseller', TopSellerView.as_view()),
    path('<pk>', RealtorView.as_view()) # 기본키로 중개업자를 찾아옴
]