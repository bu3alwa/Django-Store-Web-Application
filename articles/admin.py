from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
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

class ArticleAdmin(SummernoteModelAdmin):
    form = ArticleAdminForm
    summernote_fields = ('body',)

admin.site.register(Article, ArticleAdmin)


