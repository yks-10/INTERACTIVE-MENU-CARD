from django.contrib import admin
from .models import Item

# custom django admin
class ItemAdminView(admin.ModelAdmin):
    model = Item
    list_display = ('id', 'name', 'category', 'price')
    search_fields = ('id', 'name', 'category')


# Register your models here.
admin.site.register(Item, ItemAdminView)
