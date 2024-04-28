from django.urls import path
from .views import subscribe
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
]
