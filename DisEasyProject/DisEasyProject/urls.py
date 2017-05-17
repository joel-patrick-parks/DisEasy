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
    # these could all go into their own file but that's a task for another day
    url(r'^diabetes/submit$', MLViews.submitDiabetes),
    url(r'^diabetes/form$', UIViews.formDiabetes),
    url(r'^diabetes/result/(?P<uprob>[\d.]+)-(?P<ures>[\d.]+)-(?P<age>[\d.]+)-(?P<gender>\d+)-(?P<bmi>[\d.]+)-(?P<albu>[\d.]+)-(?P<glyco>[\d.]+)$', UIViews.resultDiabetes),

    # likewise
    url(r'^thyroid/submit$', MLViews.submitThyroid),
    url(r'^thyroid/form$', UIViews.formThyroid),
    url(r'^thyroid/result/(?P<age>[\d.]+)-(?P<gender>[\d.]+)-(?P<TSH>[\d.]+)-(?P<T3>[\d.]+)-(?P<TT4>[\d.]+)-(?P<result>[\d.]+)-(?P<accuracy>[\d.]+)-(?P<probability>[\d.]+)$', UIViews.resultThyroid),

    # generic urls - should stay here
    url(r'^about$', UIViews.about),
    url(r'^login$', UIViews.login),

    # fall-through to home page (can configure to 404 instead)
    url(r'', UIViews.home),
]
