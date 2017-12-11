from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_info = models.FileField(upload_to= 'data')

    def __unicode__(self):
        return self.user_name


KIND_CHOICES = (
    ('Python技术',  'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
)

class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default= '---',)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES,
                            default= KIND_CHOICES[0])

