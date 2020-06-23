from django.shortcuts import render
from .models import Article, Comment
from django.http import HttpResponse

def index(request):
	data = {'article_title' : Article.objects.filter(id=1)[0].article_title,
			'text' : Article.objects.filter(id=1)[0].text,
			'author' : Article.objects.filter(id=1)[0].author}
	return render(request, 'index.html', context=data)

def blog_page(request):
	data = {'Article_list': Article.objects.all()}
	return render(request, 'index.html', data)	

def article(request, article_id):
	data = {'Article': Article.objects.filter(id= article_id)}

	return render(request, 'index.html', data)