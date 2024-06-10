from django.urls import path

from chart_test import views

app_name = 'chart_test'

urlpatterns = [
    path('', views.show_chart, name='show_chart')
]