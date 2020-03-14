from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article
# Create your views here.
def article_details(request,article_id): 
    context  = {}

    article = get_object_or_404(Article,pk = article_id)
    context['article_obj'] = article
    # return HttpResponse("<h2>文章标题:{}</h2>   <br> 文章内容{}".format(article.title,article.body))
    return render(request,"article_detail.html",context)


def article_list(request): 
    articles = Article.objects.filter(is_deleted = False)
    context = {}
    context['articles'] = articles

    return render(request,"article_list.html",context)