from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Blog, BlogTag
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from read_statics.utils import read_statistics_once_read
from django.contrib.contenttypes.models import ContentType


# Create your views here.
#包含了月份信息和类型信息
def type_list_function(request):
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(
            created_time__year=blog_date.year,
            created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    # blog_types = BlogTag.objects.all()
    # blog_types_list = []
    # for blog_type in blog_types:
    #     blog_type.blog_count = Blog.objects.filter(tags=blog_type).count()
    #     blog_types_list.append(blog_type)

    #adsf;dasfjasd;fasdjf
    content = {
        'blog_types': BlogTag.objects.annotate(blog_count=Count('blog')),
        'blog_dates': blog_dates_dict
    }
    return content


def blog_details(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.filter(is_deleted=False)
    next_blog = blogs.filter(created_time__lt=blog.created_time).first()
    previous_blog = blogs.filter(created_time__gt=blog.created_time).last()
    read_cookie_key = read_statistics_once_read(request, blog)

    context = {}
    context = type_list_function(request)
    context['previous_blog'] = previous_blog
    context['next_blog'] = next_blog
    context['blog'] = blog
    response = render(request, "blog/blog_detail.html", context)
    response.set_cookie(read_cookie_key, 'true', max_age=60)  #标记 cookie
    return response


def blog_list(request):

    #获取页码参数
    page_num = request.GET.get('page', 1)
    blogs_all_lists = Blog.objects.filter(is_deleted=False)
    #分页器进行分页
    p = Paginator(blogs_all_lists, 6, request=request)
    blog_page = p.page(page_num)

    context = {}
    context = type_list_function(request)
    context['blog_pages'] = blog_page
    return render(request, "blog/blog_list.html", context)


def blog_with_type(request, blog_type_pk):
    page_num = request.GET.get('page', 1)
    blog_type = get_object_or_404(BlogTag, pk=blog_type_pk)
    blogs = Blog.objects.filter(tags=blog_type)
    p = Paginator(blogs, 6, request=request)
    blog_page = p.page(page_num)

    context = {}
    context = type_list_function(request)
    context['blog_pages'] = blog_page

    # return render(request, "blog/blog_with_type.html", context)
    return render(request, "blog/blog_list.html", context)


def blog_with_date(request, year, month):
    blogs = Blog.objects.filter(created_time__year=year,
                                created_time__month=month)
    p = Paginator(blogs, 6, request=request)
    page_num = request.GET.get('page', 1)

    blog_page = p.page(page_num)
    context = {}
    context = type_list_function(request)
    context['blog_pages'] = blog_page
    return render(request, "blog/blog_list.html", context)

    pass