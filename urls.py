from django.urls import path

from .import views

urlpatterns = [
    path("", views.home, name ='home'),
    path("calculator",views.calculator,name="calculator"),
    path("add", views.add, name='add'),
    path("sub", views.sub, name='sub'),
    path("multi", views.multi, name='multi'),
    path("div", views.div, name='div')
]