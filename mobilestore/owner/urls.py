from django.urls import path
from owner import views

urlpatterns=[
    path("add",views.add_mobile,name="addmobile")
]