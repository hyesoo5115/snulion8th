"""seminar URL Configuration

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

#seminar/seminar/url.py
from django.contrib import admin
from django.urls import path
import feedpage.views
from django.conf.urls import include
import feedpage.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',feedpage.views.index, name='index'),
    path('feeds/', include('feedpage.url')), #feed/까지 자르고 feedpage.url.py 로 보냄
    # path('accounts/', include('accounts.urls')), #추가
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/modify/', accounts.views.modify, name='modify'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
