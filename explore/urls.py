from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/', views.PlaceRetrieveAPIView.as_view(), name='place')
]