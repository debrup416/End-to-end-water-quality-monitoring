from django.urls import path

from . import views

urlpatterns = [
   path('',views.getDataAndPredict,name="water-predict"),
]

