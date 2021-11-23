from django.urls import path
from home import views
from .views import *
urlpatterns=[
      path('',views.IndexView.as_view(),name='home'),
      path('matea',views.MateaView.as_view(),name='matea'),
]