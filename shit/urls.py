from django.urls import path
from . import views

app_name = "shits"
urlpatterns = [
    path('', views.shit_list, name="list"),
    path('create',views.create_shit,name="create"),
    path('<slug>',views.shit_detail, name= "detail"),
]
