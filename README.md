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