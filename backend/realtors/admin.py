from django.contrib import admin
from .models import Realtor

#중개업자 관리하는 어드민
class RealtorAdmin(admin.ModelAdmin):
    #어드민 패널에서 보여줄것들 
    list_display = ('id', 'name', 'email', 'date_hired')
    #중개업자를 보기위해 클릭하는 링크
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)

