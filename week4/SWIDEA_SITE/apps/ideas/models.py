from django.db import models
from apps.devtools.models import Devtool

class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    image = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.CharField('아이디어 설명', max_length=500)
    interest = models.IntegerField('아이디어 관심도', default=0)
    # 개발툴 - FK 활용
    # devtool = models.ForeignKey(Devtool, on_delete=models.SET_NULL, verbose_name='개발툴', null=True) # 개발툴 사라져도 SET_NULL지정을 통해 null로 바꿈