from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name="add_todo"),
    path('admin/', admin.site.urls),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]
