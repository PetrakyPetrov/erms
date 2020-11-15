from django.urls import path
from hr import views

urlpatterns = [
    path('', views.index),
    path('add', views.createEmployee),
    path('edit/<int:id>', views.updateEmployee, name='edit-employee'),
    path('delete/<int:id>', views.deleteEmployee, name='delete-employee')
]
