from django.db import models
from datetime import datetime


class Realtor(models.Model):

    """부동산 중개업자를 위한 모델"""
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # 업로드된 이미지를 연도,달,일 순으로 정렬
    description = models.TextField(blank=True)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name