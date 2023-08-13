from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('add_tasks/', views.TaskFormView.as_view(), name='add_tasks'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('edit_task/<int:pk>', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>',views.DeleteTaskView.as_view(), name='delete_task'),
    path('complete_task/<int:pk>',views.complete_task, name='complete_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
]