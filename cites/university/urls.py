from django.urls import path
from .views import  *


app_name = 'university'

urlpatterns =[
    path('', PostListView.as_view(), name='list'),
    path("<int:pk>/",PostDetailView.as_view(), name='post'),
    path("contact/", Contact, name='contact')

]


