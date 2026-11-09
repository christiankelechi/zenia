"""
URL configuration for blankexchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path,re_path,include
from zenia_app_root.geometries_management.viewsets.cube import CubeViewset
schema_view = get_schema_view(
   openapi.Info(
      title="Zenia App Api",
      default_version='v1',
      description="Xpresscad App Ai Model Documentation, make sure to abide to terms and conditions of using these Api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kezechristian@gmail.com"),
      license=openapi.License(name="xpresscad licence"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
   url="https://zeniaapi.duckdns.org/api/docs/"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('',include(('zenia_app_root.voice_recognition.routers','zenia_app_root.voice_recognition'))),
    #  path('blender/', include('zenia_app_root.geometries_management.urls')),
    path('',include(('zenia_app_root.geometries_management.routers.sphere','zenia_app_root.geometries_management'))),
    path('',include(('zenia_app_root.geometries_management.routers.cube'))),
  
    path('',include(('zenia_app_root.geometries_management.routers.rectangle'))),
    path('',include(('zenia_app_root.geometries_management.router'))),
    
    path('',include(('zenia_app_root.geometries_management.routers.message_prompt','zenia_app_root.geometries_management.routers'))),
    path('',include(('zenia_app_root.security.user.routers','zenia_app_root.security.user'))),
    path('',include(('zenia_app_root.security.auth.routers','zenia_app_root.security.auth'))),
    path('cad-upload/', CubeViewset.as_view({'post': 'create'}), name='cad-upload'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)