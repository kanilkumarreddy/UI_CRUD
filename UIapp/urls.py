from django.urls import path,include
from . import views
# 
from .views import Customerview
urlpatterns=[
# UI_urls
    path('',views.list,name="list"),
    path('insert',views.insert,name="insert"),
    path('insert1',views.insert1,name="insert1"),
    path('get/<int:id>/',views.get,name="get"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),

# api_urls
    path('customers/',views.list1,name="List"),
    path('customers/<int:id>/',views.get1,name="Get"),
    path('customer/create/',views.create1,name="Create"),
    path('customer/update/<int:id>/',views.update1,name="Update"),
    path('customer/delete/<int:id>/',views.delete1,name="Delete")
]