from django.db import models
from django.core.exceptions import ValidationError
from blog.core.const import CONST

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("categories.Category")

    def clean(self):
        if self.pk and self.categories.count() > CONST.MAX_CATEGORY_LIMIT:
            raise ValidationError("At most 6 categories can be added to a post.")

    def __str__(self):
        return self.title