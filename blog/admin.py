from django.contrib import admin
from .models import Post, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published', 'status')
	list_filter = ('status', 'created', 'published', 'author')
	search_fields = ('title', 'content')
	prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user','email','approved')

admin.site.register(Comment, CommentAdmin)


