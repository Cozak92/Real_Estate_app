from rest_framework import serializers
from .models import Listing

"""1. 모든 필드를 리턴하는 시리얼라이저 
    2. 특정 필드를 리턴하는 시리얼라이저"""


#목록을 표현하는 시리얼라이저 모든 데이터를 넘겨줄 필요없이 특정 필드값만 넘김
class ListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug' )

#유저가 클릭했을시 보여줄것이므로 모든필드를 넘겨준다
class ListingDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'