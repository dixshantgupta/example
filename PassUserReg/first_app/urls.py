from first_app import views
from django.urls import path
app_name = 'first_app'
urlpatterns=[
path('register/',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),
]
