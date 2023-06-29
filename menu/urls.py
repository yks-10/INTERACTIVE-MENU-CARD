from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HealthView.as_view(), name="Health-Check"),
    path('item/', views.ItemView.as_view(), name="item"),
]
