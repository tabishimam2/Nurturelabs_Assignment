"""solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
path('admin/advisor/',views.AdvisorApi.as_view()),
path('admin/', admin.site.urls),
path('user/register/',views.UserApi.as_view()),
path('user/login/', views.UserLogin.as_view()),
path('user/<int:pk>/advisor/',views.AdvisorList.as_view()),
path('user/<int:pk>/advisor/<int:fk>/',views.Bookings.as_view()),
path('user/<int:pk>/advisor/booking/',views.SeeBookings.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

