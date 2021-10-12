from django.urls import path
from bookapp import views
urlpatterns=[
    path("add",views.add_book,name="bookadd")
]