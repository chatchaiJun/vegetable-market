from django.urls import path
from . import views

urlpatterns = [
      path('login',views.login_user,name='login'),
      path('register',views.register,name='register'),
      # path('address',views.create_address,name='address'),
      path('logout',views.logout_user,name="logout")
]