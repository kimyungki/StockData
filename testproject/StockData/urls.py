from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('output/', views.output),
    path('output2/', views.output2),
    path('output3/', views.output3),
    path('predict/', views.predict),
    path('predict2/', views.predict2),
    path('predict3/', views.predict3)
]

