from django.shortcuts import render
from .models import Article, Comment
from django.http import HttpResponse

def index(request):
	data = {'article_title' : Article.objects.filter(id=1)[0].article_title,
			'text' : Article.objects.filter(id=1)[0].text,
			'author' : Article.objects.filter(id=1)[0].author}
	return render(request, 'index.html', context=data)

def about_me(request):
	data = {'article_title' : Article.objects.filter(id=2)[0].article_title,
			'text' : Article.objects.filter(id=2)[0].text,
			'author' : Article.objects.filter(id=2)[0].author}
	return render(request, 'index.html', context = data)	