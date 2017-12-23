from django.contrib import admin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published', 'status')
	list_filter = ('status', 'created', 'published', 'author')
	search_fields = ('title', 'content')
	prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
