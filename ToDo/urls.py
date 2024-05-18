
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.todo_list,name='home'),
    path('create/',views.todo_create,name='new_task'),
    path('edit/<int:pk>',views.todo_edit, name='edit'),
    path('delete/<int:pk>',views.todo_delete, name='delete'),
    path('complete/<int:pk>',views.todo_complete, name='complete'),
    path('delete_all/',views.todo_delete_all, name='delete_all'),
    path('register/',views.registro, name='register'),
    
]
