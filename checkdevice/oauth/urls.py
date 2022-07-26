from django.urls import path

from . import views


# для того, чтобы псевдонимы 'detail' различать и не путать в разных приложениях
app_name = 'oauth'
urlpatterns = [
    path('', views.o_auth, name='o_auth'),
]