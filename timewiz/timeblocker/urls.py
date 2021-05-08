from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('googlepermission/', views.googlepermission, name='google permission'),
    path('googlepermission/redirect/', views.googleredirect, name='google redirect')
]

