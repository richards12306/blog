from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete = models.CASCADE,default = 1)#一对一外键，关联作者模型
    is_deleted = models.BooleanField(default=False)
    update_time = models.DateTimeField(auto_now = True)#更新日期
