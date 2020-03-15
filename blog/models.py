from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
import datetime
from mdeditor.fields import MDTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from read_statics.models import ReadNumExpandMethod,ReadDetail
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class BlogTag(models.Model):
    """博客分类"""
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=150)
    content = MDTextField()
    created_time = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               default=1)  #一对一外键，关联作者模型
    tags = models.ForeignKey(BlogTag, on_delete=models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)
    read_details = GenericRelation(ReadDetail)
    abstraction = models.TextField(max_length=150, default="nothing left")
    last_update_time = models.DateTimeField(auto_now=True)  #更新日期

    def __str__(self):
        return "<Blog:{}>".format(self.title)

    class Meta:
        ordering = ['-created_time']
        


# class ReadNum(models.Model):
#     read_num = models.IntegerField(default=0)
#     blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)
