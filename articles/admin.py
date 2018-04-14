from django.contrib import admin
from django import forms
from .models import Article

class ArticleAdminForm(forms.ModelForm):
    slug = forms.SlugField(
            required=False,
            widget=forms.TextInput(attrs={'readonly':'readonly'})
            )

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)


