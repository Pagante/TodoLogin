from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name="signup"),
    path('TodoAppList/', views.TodoAppList, name='TodoAppList'),
    path('add/', views.addTodoList, name='add'),
    path('completed/<user_id>', views.completeTodo, name='completed'),
    path('deleteCompleted', views.deleteCompleted, name='deleteComplete'),
    path('delete', views.deleteAll, name='deleteAll')

]