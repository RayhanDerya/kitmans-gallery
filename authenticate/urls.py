from django.urls import path
from authenticate.views import login,register,logout

app_name = 'authenticate'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]