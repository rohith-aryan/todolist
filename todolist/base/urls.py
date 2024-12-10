from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create/', views.task_create, name='task_create'),
    path('tasks/', views.task_list, name='task_list'),  
    path('tasks/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='task_delete'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
