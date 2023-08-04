from django.contrib import admin
from django.urls import path
from menu import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Menu Card",
        default_version='v1',
        description="single api",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', views.HealthView.as_view(), name="Health-Check"),
    path('item/', views.ItemView.as_view(), name="item"),
]
