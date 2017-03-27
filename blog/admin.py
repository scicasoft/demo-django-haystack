from django.contrib import admin

from blog.models import Auteur, Article, Commentaire, Tag, Categorie

admin.site.register(Auteur)
admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(Tag)
admin.site.register(Categorie)