"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from task.views import CustomUserViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"auth/users", CustomUserViewSet, basename="custom-user")

# urlpatterns = [
#     path('api/', include('task.routes')),
#     path('admin/', admin.site.urls),
#     # path('task/', include('task.routes')),
#     # Djoser authentication routes
#     path('api/auth/', include('djoser.urls')),
#     path('api/auth/', include('djoser.urls.jwt')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="custom-user")  # note: no 'auth/' prefix

urlpatterns = [
    path('api/auth/', include(router.urls)),  # <-- your custom viewset first
    path('api/auth/', include('djoser.urls')),  # Djoser fallback
    path('api/auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Register
# curl -X POST http://127.0.0.1:8000/api/auth/users/ \
#   -H "Content-Type: application/json" \
#   -d '{"username":"houy123","password":"123","email":"houy1212@gmail.com"}'