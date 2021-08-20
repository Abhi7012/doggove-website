from django.urls import path
from adddog import views
urlpatterns=[
    path('',views.hello,name="hello"),
]