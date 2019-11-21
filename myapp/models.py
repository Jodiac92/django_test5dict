from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    #일반테이블
    
    def as_dict(self):
        return {'name':self.name, 'age':self.age} #테이블 dict타입으로 만들어주기