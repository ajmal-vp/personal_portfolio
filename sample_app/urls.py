from django.urls import path

from sample_app import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('', views.index, name="index")

]