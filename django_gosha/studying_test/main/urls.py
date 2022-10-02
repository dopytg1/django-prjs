from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('about-us', views.about_us, name='about'),
    path('create-goal', views.create_goal, name='create-goal'),
    path('change/<int:id>/', views.change_goal),
    path('delete/<int:id>/', views.delete_goal)
]
