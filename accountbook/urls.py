from django.urls import path

from accountbook import views

app_name = 'accountbook'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category_list'),
]
