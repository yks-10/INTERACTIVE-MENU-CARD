from django.contrib import admin
from .models import Item

# custom django admin
class ItemAdminView(admin.ModelAdmin):
    model = Item
    list_display = ('id', 'name', 'category', 'price', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('id', 'name', 'category')


# Register your models here.
admin.site.register(Item, ItemAdminView)
