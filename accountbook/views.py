from datetime import timedelta

from django.db.models import Sum, Min, Max
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from accountbook.forms import AccountBookForm
from accountbook.models import Category, AccountBook


class CategoryListView(ListView):
    model = Category  # Category 테이블 모든 Category 가져와서 -> category_list라는 context에 담아 category_list.html에 넘긴다


class AccountBookListView(ListView):
    model = AccountBook


class AccountBookCreateView(CreateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('accountbook:accountbook_dashboard')


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


def get_all_chart_data(request):
    all_category_total_price_qs = AccountBook.objects.all() \
        .values('category__name', 'category__bgcolor').annotate(total_price=Sum('price')) \
        .order_by('-total_price')
    date_range = AccountBook.objects.aggregate(
        start_date=Min('time'),
        end_date=Max('time'),
    )

    all_category_total_price_list = list(all_category_total_price_qs)

    context = {
        'weekly_category_total_price_list': all_category_total_price_list,
        'start_date': date_range["start_date"].date(),
        'end_date': date_range["end_date"].date(),
    }

    return JsonResponse(context)


def accountbook_createform(request):
    if request.method == 'POST':
        form = AccountBookForm(request.POST)
        if form.is_valid():     #사용자가 입력한 값이 제대로 되었는지 확인하자
            form.save()         #사용자가 입력한 값으로 DB에 저장하자
            return redirect('accountbook:accountbook_dashboard')
    else:
        form = AccountBookForm()

    return render(request, 'accountbook/accountbook_createform.html', {'form': form})
