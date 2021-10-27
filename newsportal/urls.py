"""newsportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/<int:id>',views.views_more,name='views_more'),
    path('logout',views.signout,name='signout'),
    path('create_post/',views.create_post,name='create_post'),
    path('about/',views.about),
    path('login/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.signup,name ='signup')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
