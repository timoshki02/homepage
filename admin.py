from django.contrib import admin
from .models import NewsPost,Comment

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','body','publish','created','updated')
	list_filter = ('created','updated','publish')
	search_fields = ('title','body')
	prepopulated_fields = {'slug' : ('title',)}
	date_hierarchy = ('publish')

admin.site.register(NewsPost,NewsAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','post','created','active')
	list_filter = ('active','created','updated')
	search_fields = ('name','email','body')
admin.site.register(Comment,CommentAdmin)


