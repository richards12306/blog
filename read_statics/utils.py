from django.contrib.contenttypes.models import ContentType
from .models import ReadNum, ReadDetail
from django.utils import timezone
import datetime
from django.db.models import Sum


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "{}_{}_read".format(ct.model, obj.pk)

    if not request.COOKIES.get(key):
        #判断是否存在对应的阅读数量
        #总阅读数
        readnum, created = ReadNum.objects.get_or_create(content_type=ct,
                                                         object_id=obj.pk)

        readnum.read_num += 1
        readnum.save()
        #当天阅读数
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(
            content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()

    return key


def get_week_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime("%m/%d"))

        read_details = ReadDetail.objects.filter(content_type=content_type,
                                                 date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


def get_today_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type,
                                             date=today).order_by('-read_num')
    return read_details[:3]


def get_week_hot_data(content_type):
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    read_details = ReadDetail.objects.filter(content_type=content_type, date__lt=today,date__gte=date) \
                .values('content_type', 'object_id') \
                .annotate(read_num_sum=Sum('read_num'))\
                .order_by('-read_num_sum')
    return read_details
