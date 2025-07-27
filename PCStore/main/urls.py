from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home_view , name="home_view"),
    path('base/', views.base_view , name="base_view"),
    path('contact/', views.contact_view , name="contact_view"),
    path('contact/messages/', views.contact_messages_view , name="contact_messages_view"),
    path('contact/messages/delete/', views.delete_all_contacts, name="delete_all_contacts"),
    path('login/', views.login_view , name="login_view"),
    path('register/', views.register_view , name="register_view"),
    path('logout/', views.logout_view , name="logout_view"),
    path('users/', views.users_list_view, name='users_list_view'),
]
