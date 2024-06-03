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