from django.urls import path
from testapp.views import home,register,Login_User,Logout_User

urlpatterns = [
    path('', home,name='home'),
    path('register/', register,name='register'),
    path('login/', Login_User,name='login'),
    path('logout/', Logout_User,name='logout'),

]
