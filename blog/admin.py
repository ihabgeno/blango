from django.contrib import admin
from blog.models import Tag, Post

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')
  #list_display = ('summary','content')
  #list_display =["title","published_at"]
  
# Register your models here.
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
