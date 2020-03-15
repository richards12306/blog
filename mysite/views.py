from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from read_statics.models import ReadNum, ReadDetail
from read_statics.utils import get_week_read_data, get_today_hot_data, get_week_hot_data
from blog.models import Blog
from django.utils import timezone
import datetime
from django.db.models import Sum
from django.core.cache import cache


def get_week_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lt=today,
                                read_details__date__gte=date)\
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num'))\
                .order_by('-read_num_sum')
    return blogs


def home(request):
    context = {}
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_week_read_data(blog_content_type)
    today_hot_blogs = get_today_hot_data(blog_content_type)
    #获取七天热门博客的数据
    week_hot_blogs = cache.get('week_hot_blogs')
    if week_hot_blogs is None:
        week_hot_blogs = get_week_hot_blogs()
        cache.set('week_hot_blogs', week_hot_blogs, 3600)
        print('df')
    else:
        print('cache')

    context = {
        'read_nums': read_nums,
        'dates': dates,
        'today_hot_blogs': today_hot_blogs,
        'week_hot_blogs': week_hot_blogs,
    }
    return render(request, 'home.html', context)
