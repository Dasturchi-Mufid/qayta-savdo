from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('customers/<str:branch>/',views.customers_list,name='customers'),
    path('customer/<int:id>/',views.customer_detail,name='customer_detail'),
    path('comment-create/',views.create_comment,name='create_comment'),

    path('sellers/<str:branch>/',views.seller_list,name='seller_list'),
    # path('seller/<int:id>/',views.seller_detail,name='seller_detail'),
    # path('seller/<int:id>/<int:s_id>',views.seller_detail,name='seller_detail_s_id'),
    re_path(r'^seller/(?P<id>\d+)/(?P<s_id>\d+)?$', views.seller_detail, name='seller_detail'),
    path('upload/',views.upload_excel,name='upload_excel')
    
]