"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# импорт для аутентификации через github
from django.urls import path, include, re_path
# create obj of routers
from rest_framework import routers

from companycheck.views import CompanyCheckViewSet
from companyuse.views import CompanyUseViewSet
from classofdevice.views import ClassOfDeviceViewSet
from intervalcheck.views import IntervalCheckViewSet
from typeofsi.views import TypeOfSiViewSet

from oauth.views import o_auth

router = routers.SimpleRouter()
# # create url for router and view
router.register(r'companycheck', CompanyCheckViewSet, )
router.register(r'companyuse', CompanyUseViewSet)
router.register(r'classofdevice', ClassOfDeviceViewSet)
router.register(r'intervalcheck', IntervalCheckViewSet)
router.register(r'intervalcheck', TypeOfSiViewSet)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('auth/', o_auth),
    re_path('', include('social_django.urls', namespace='social')),
]
# add url to urlpatters
urlpatterns += router.urls
