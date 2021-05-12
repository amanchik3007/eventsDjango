from django.urls import path
from events import views

urlpatterns = [
    path('',                  views.eventList, name='events'),
    path('detail/<str:pk>/',  views.eventDetail, name='detail'),
    path('create/',           views.createEvent, name='create'),
    path('update/<str:pk>/',  views.eventUpdate, name='update'),
    path('delete/<str:pk>/',  views.eventDelete, name='delete'),
]