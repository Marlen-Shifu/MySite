from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name = 'index'),
	path('blog/', views.blog_page, name = 'blog_page'),
	path('blog/<int:article_id>', views.article, name = 'article'),
]