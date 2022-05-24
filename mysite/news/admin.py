from django.contrib import admin

from .models import News
from .models import Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(News, NewsAdmin)

admin.site.register(Category,CategoryAdmin)

