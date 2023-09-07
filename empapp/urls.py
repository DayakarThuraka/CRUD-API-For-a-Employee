from django.contrib import admin
from django.urls import path
from empapp import views

urlpatterns = [
    path('emp/',views.EmpDataView.as_view()),
    path('update/<int:pk>',views.EmpDataUpdate.as_view())
]