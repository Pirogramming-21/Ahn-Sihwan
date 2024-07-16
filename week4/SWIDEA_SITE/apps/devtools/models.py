from django.db import models

class Devtool(models.Model):
    name = models.CharField('이름', max_length=24)
    kind = models.CharField('종류', max_length=24)
    content = models.CharField('개발툴 설명', max_length=500)

    def __str__(self):
        return self.name