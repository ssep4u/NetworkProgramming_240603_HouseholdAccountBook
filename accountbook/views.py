from django.shortcuts import render
from django.urls import reverse_lazy
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
    accountbook_list = AccountBook.objects.all()      #all(): 전체, filter(): 필터링, get(): 하나 가져옴, none(): 안 가져옴
    context = {
        'accountbook_list': accountbook_list,
    }
    return render(request, 'accountbook/accountbook_dashboard.html', context=context)