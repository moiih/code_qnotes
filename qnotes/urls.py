from django.urls import path
from notes import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('change_user_password/', views.change_password, name='change_password'),
    path('', views.home, name='home'),

    # path('login/', views.login_notes, name='login'),
    path('authentication/', views.login_notes, name='login'),
    path('logout/', views.logout_notes, name='logout'),
]
