from django.db import models

class Article(models.Model):
	
	article_title = models.CharField('Название статьи', max_length=50)
	
	text = models.TextField('Текст статьи')

	author = models.CharField('Автор статьи', max_length=30, default = 'Admin')

	def __str__(self):
		return self.article_title

class Comment(models.Model):

	comment = models.ForeignKey(Article, on_delete=models.CASCADE)

	author = models.CharField('Автор комментария', max_length=30, default = 'User')

	text = models.CharField('Текст комментария', max_length=200)
	
	def __str__(self):
		return self.article_title