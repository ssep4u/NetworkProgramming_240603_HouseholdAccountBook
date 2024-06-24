from datetime import timedelta

from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from accountbook.models import Category, AccountBook


class CategoryListView(ListView):
    model = Category  # Category 테이블 모든 Category 가져와서 -> category_list라는 context에 담아 category_list.html에 넘긴다


class AccountBookListView(ListView):
    model = AccountBook


class AccountBookCreateView(CreateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('accountbook:accountbook_list')


class AccountBookUpdateView(UpdateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('accountbook:accountbook_list')


class AccountBookDeleteView(DeleteView):
    model = AccountBook
    success_url = reverse_lazy('accountbook:accountbook_list')


def dashboard_accountbook(request):
    accountbook_list = AccountBook.objects.all()  # all(): 전체, filter(): 필터링, get(): 하나 가져옴, none(): 안 가져옴
    context = {
        'accountbook_list': accountbook_list,
    }
    return render(request, 'accountbook/accountbook_dashboard.html', context=context)


def get_daily_accountbook_list(request, year, month, date):
    specific_date = datetime(year, month, date).date()

    daily_accountbook_list = AccountBook.objects.filter(time__range=(specific_date, specific_date + timedelta(days=1)))

    context = {
        'date': f'{year}.{month}.{date}',
        'daily_accountbook_list': daily_accountbook_list,
    }
    return render(request, 'accountbook/daily_accountbook_list.html', context=context)


def get_week_range(date):
    start_of_week = date - timedelta(days=date.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday
    return start_of_week, end_of_week


def get_weekly_chart_data(request, year, month, date):
    given_date = datetime(year, month, date).date()
    start_of_week, end_of_week = get_week_range(given_date)

    weekly_category_total_price_qs = AccountBook.objects.filter(time__range=(start_of_week, end_of_week)) \
        .values('category__name', 'category__bgcolor').annotate(total_price=Sum('price')) \
        .order_by('-total_price')

    weekly_category_total_price_list = list(weekly_category_total_price_qs)  # QuerySet -> list

    context = {
        'weekly_category_total_price_list': weekly_category_total_price_list,
        'start_date': start_of_week,
        'end_date': end_of_week,
    }

    return JsonResponse(context)
