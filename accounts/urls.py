from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home ,name = "home"),
    path('product/',views.products,name = "products"),
    path('customer/<str:pk_test>/',views.customer,name = "customer"),
    path('create_order/<str:pk>',views.createorder,name = "create_order"),
    path('update_order/<str:pk>',views.updateorder,name = "update_order"),
    path('delete_order/<str:pk>',views.deleteorder,name = "delete_order"),
]