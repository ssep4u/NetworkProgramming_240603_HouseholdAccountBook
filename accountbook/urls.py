from django.urls import path

from accountbook import views

app_name = 'accountbook'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('', views.AccountBookListView.as_view(), name='accountbook_list'),
    path('create/', views.AccountBookCreateView.as_view(), name='accountbook_create'),
    path('update/<int:pk>/', views.AccountBookUpdateView.as_view(), name='accountbook_update'),
    path('delete/<int:pk>/', views.AccountBookDeleteView.as_view(), name='accountbook_delete'),
]
