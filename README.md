# 가계부(Household Account Book)
1. startproject householdAccountBook
   1. python -m pip install django~=4.2
   2. django-admin startproject householdAccountBook .
   3. File > Settings... > Language & Frameworks > Django > [v] Enable Django Support
   4. Run > Edit Configurations... > + Django Server > Name: runserver
   5. VCS > Enable Version Control Integration... > git > ok
2. 차트용 실습: startapp chart_test
   1. python manage.py startapp chart_test
   2. settings > INSTALLED_APPS > 'chart_test', 
3. chart_test/
   1. views
      1. show_chart()
   2. templates
      1. chart_view.html
   3. urls
      1. chart_test:show_chart
4. 프로젝트명/
   1. urls
      1. include('chart_test.urls')
   2. data/data.json
      1. 임시 데이터
5. startapp accountbook
   1. python manage.py startapp accountbook
   2. settings.py > INSTALLED_APPS > 'accountbook',
6. accountbook/
   1. models
      1. Category
         1. name, bgcolor
      2. AccountBook
         1. type(0: 지출, 1: 소비), price, category, time, contents, created_at, updated_at
         2. ~~photo~~
      3. python manage.py makemigrations accountbook
      4. python manage.py migrate
   2. admin
      1. Category
      2. AccountBook
      3. python manage.py createsuperuser
   3. views
      1. CategoryListView
   4. templates
      1. category_list.html
   5. urls
      1. accountbook:category_list







