"""
URL configuration for ecomproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from physicaldb.views import (
    MuscleGroupViewSet, ExerciseCategoryViewSet, EquipmentViewSet, ExerciseViewSet, exercises_page
)

router = DefaultRouter()
router.register(r'muscle-groups', MuscleGroupViewSet)
router.register(r'categories', ExerciseCategoryViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'exercises', ExerciseViewSet)


urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('diet_plans.urls')),
    path('', include('diet_plans1.urls')),
    path('', include('height_growth.urls')),
    path('', include('gymlocator.urls')),
    path('', include('contactus.urls')),
    path('', include('meditation1.urls')),
    path('', include('yoga1.urls')),
    path('services/', include('services.urls')),
    path('privacy-policy/', include('privacy.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API Endpoints
   
    
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),  # Add Debug Toolbar URLs
    ] + urlpatterns


