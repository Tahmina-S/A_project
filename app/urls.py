from django.urls import path
from app.views import home,table,delete,form,update
urlpatterns = [
    path('', home),
    path('form/', form, name='c'),
    path('table/', table, name='r'),
    path('update/<str:b>', update, name='u'),
    path('delete/<str:a>', delete, name='d'),

]