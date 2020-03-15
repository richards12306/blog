from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from read_statics.models import ReadNum, ReadDetail
from read_statics.utils import get_week_read_data
from blog.models import Blog


def home(request):
    context = {}
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_week_read_data(blog_content_type)


    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    return render(request, 'home.html', context)
