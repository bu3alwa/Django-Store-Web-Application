from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db.models.manager import EmptyManager

class Article(models.Model):
    slug = models.SlugField(
            _("Slug"),
            db_index=True,
            unique=True,
            max_length=255)

    title = models.CharField(
            _("Title"),
            db_index=True,
            max_length=255)

    body = models.TextField(_("Body"))
    date = models.DateField(_("Date"))

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)


    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,num)
            num +=1
        return unique_slug

    def get_absolute_url(self):
        return reverse('articles.views.article_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Article, self).save(*args, **kwargs)


