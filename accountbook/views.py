from django.shortcuts import render
from django.views.generic import ListView

from accountbook.models import Category


class CategoryListView(ListView):
    model = Category    #Category 테이블 모든 Category 가져와서 -> category_list라는 context에 담아 category_list.html에 넘긴다
