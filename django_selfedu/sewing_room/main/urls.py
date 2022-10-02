from django.urls import path
from . import views


urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('assortment', views.Assortment.as_view(), name='products'),
    path('category/<slug:cat_slug>/', views.ShowCategory.as_view(), name='category'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
]
