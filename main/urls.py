from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Quiz documentation",
      default_version='V1',
      description="Quiz API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kubat.usubaliev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include('quiz.urls')),
    path('staff/', include('staff.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Quiz admin'
admin.site.site_title = 'Quiz portal'
admin.site.index_title = 'Welcome to Quiz Portal'
