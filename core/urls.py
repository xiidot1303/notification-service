"""fabrique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from app.views.client import *
from app.views.newsletter import *


urlpatterns = [
    path('xiidot1303/', admin.site.urls),

    # Client
    path('client_create', client_create),
    path('client_edit/<int:pk>', client_edit),
    
    # Newsletter
    path('newsletter_create', newsletter_create),
    path('newsletter_edit/<int:pk>', newsletter_edit),
    path('newsletter_overall_statistics', newsletter_overall_statistics),
    path('newsletter_statistic/<int:pk>', newsletter_statistic),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)