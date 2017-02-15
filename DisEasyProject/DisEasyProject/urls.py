"""DisEasyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ML import views as MLViews
from UI import views as UIViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 'submission' endpoint - where ML analysis is run
    url(r'^submit$', MLViews.submit),

    # actual UI pages
    url(r'^form$', UIViews.form),
    url(r'^result/(\d+)-(\d+)-(\d+)$', UIViews.result),
    url(r'^result/', UIViews.result),

    # fall-through to home page (can configure to 404 instead)
    url(r'', UIViews.home),
]
