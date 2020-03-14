#下级路由文件 上级处理后的 url 文件会匹配进入下级进行处理。
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('<int:blog_id>', views.blog_details, name="blog_detail"),
    path('type/<int:blog_type_pk>',
         views.blog_with_type,
         name="blog_with_type"),
    path('date/<int:year>/<int:month>',
         views.blog_with_date,
         name="blog_with_date"),
    # path('asdfasfdafads')
]
