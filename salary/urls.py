from django.urls import path
from salary import views
urlpatterns = [
    path('', views.index),

]
