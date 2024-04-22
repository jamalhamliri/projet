"""
Admin
"""
from django.contrib import admin

from .models import Article, ArticleType, Slide, Events, EmploisTemps, Niveau, Filiere

admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(Slide)
admin.site.register(Events)
admin.site.register(EmploisTemps)
admin.site.register(Niveau)
admin.site.register(Filiere)
