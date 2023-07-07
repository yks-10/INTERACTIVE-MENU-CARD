from django.db import models
from .constants import *
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Item(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY, default=FRESH_JUICE, null=False, blank=False)
    price = models.CharField(max_length=5, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['-pk']

    def __str__(self):
        return str(self.name)

