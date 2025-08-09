from django.db import models
from django.core.exceptions import ValidationError
from blog.core.const import CONST
from blog.core.errors import Messages
from django.conf import settings 

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        null = True,
        blank = True
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("categories.Category")

    def clean(self):
        if self.pk and self.categories.count() > CONST.MAX_CATEGORY_LIMIT:
            raise ValidationError(Messages.TOO_MANY_CATEGORIES)

    def __str__(self):
        return self.title