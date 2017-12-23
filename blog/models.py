from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

#category
class Category(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique=True)

	class meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_plural_name = 'categories'

	def __str__(self):
		return self.name
			
		

#post
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	category = models.ForeignKey(Category)
	slug = models.SlugField(max_length=250, unique=True)
	content = models.TextField()
	seo_title = models.CharField(max_length=250)
	seo_description = models.CharField(max_length=250)
	author = models.ForeignKey(User, related_name='blog_posts')
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.slug])

	def __str__(self):
		return self.title