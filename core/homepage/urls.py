from django.urls import path

from core.homepage.views import IndexView, AboutView, MusicaView, RadioView,RadioOnlineView
from core.homepage import views

app_name = 'home'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('radioOnline/', RadioOnlineView.as_view(), name='radio_online'),
    path('musica/', MusicaView.as_view(), name='musica'),
    path('radio/', RadioView.as_view(), name='radio'),
     path('radiOnline/', RadioOnlineView.as_view(), name='radioOnline'),
    path('galery/', views.gallery , name='galery_list'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),


]
