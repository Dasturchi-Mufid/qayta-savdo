from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('customers/<str:branch>/',views.customers_list,name='customers'),
    path('customer/<int:id>/',views.customer_detail,name='customer_detail'),
    path('comment-create/',views.create_comment,name='create_comment'),

    path('sellers/<int:id>',views.seller_detail,name='seller_detail'),
    
]