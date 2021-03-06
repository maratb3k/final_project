"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from project.views import BookViewSet, JournalViewSet
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")
router.register(r'journals', JournalViewSet, basename="journals")
# router.register(r'login', obtain_jwt_token)

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('project/', include('project.urls'))
    path('project/', include(urlpatterns)),
    path('login/', obtain_jwt_token)
]
