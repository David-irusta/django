# urls for account app
from django.urls import path
#urls for auth views
from django.contrib.auth import views as auth_views
# views for accounts app
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout_message.html'), name='logout'),
    path('signup/', views.SignUpView.as_view(template_name= 'account/signup.html'), name='signup'),
    path(
        'logout_message',
        views.LogoutMessageView.as_view(template_name='account/logout_message.html'),
        name='logout_message'
    ),
]