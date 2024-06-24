from django.urls import path

from accountbook import views

app_name = 'accountbook'

urlpatterns = [
    path('', views.dashboard_accountbook, name='accountbook_dashboard'),
    path('daily/<int:year>/<int:month>/<int:date>/', views.get_daily_accountbook_list, name='daily_accountbook_list'),
    path('weekly/<int:year>/<int:month>/<int:date>/', views.get_weekly_chart_data, name='weekly_chart_data'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('list/', views.AccountBookListView.as_view(), name='accountbook_list'),
    path('create/', views.AccountBookCreateView.as_view(), name='accountbook_create'),
    path('update/<int:pk>/', views.AccountBookUpdateView.as_view(), name='accountbook_update'),
    path('delete/<int:pk>/', views.AccountBookDeleteView.as_view(), name='accountbook_delete'),
]
