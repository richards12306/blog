#下级路由文件 上级处理后的 url 文件会匹配进入下级进行处理。
from django.urls import path
from . import views 
urlpatterns = [
    path('<int:article_id>',views.article_details,name="article_detail"),
    path('',views.article_list,name = "article_list"),
 
]
