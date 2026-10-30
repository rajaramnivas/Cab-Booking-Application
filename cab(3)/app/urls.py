from django.contrib import admin
from django.urls import path
from .views import home,register,user_login,user_logout,book_ride,my_rides,avaliable_rides,update_status,accept_rides,driver_rides
urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('book/',book_ride,name='book_ride'),
    path('my-rides/',my_rides,name='my_rides'),
    path('available-rides/',avaliable_rides,name='avaliable_rides'),
    path('accept/<int:ride_id>/',accept_rides,name='accept_rides'),
    path('driver-rides/',driver_rides,name='driver_rides'),
    path('status/<int:ride_id>/<str:status>/',update_status,name='update_status'),
]
