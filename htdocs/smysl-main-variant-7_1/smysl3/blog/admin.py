from django.contrib import admin
from .models import Article, Additional, Profile, Comment
admin.site.register(Profile)
admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Additional)
class AdditionalAdmin(admin.ModelAdmin):
    pass

