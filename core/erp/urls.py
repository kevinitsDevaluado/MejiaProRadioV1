from django.urls import path

from core.erp.views.dashboard.views import DashboardView

from core.erp.views.music.views import MusicListView,MusicCreateView,MusicUpdateView,MusicDeleteView

from core.erp.views.live.views import LiveListView,LiveCreateView,LiveUpdateView,LiveDeleteView

from core.erp.views.category.views import CategoryListView,CategoryCreateView,CategoryUpdateView,CategoryDeleteView
from core.erp.views.publicidad.views import AdvertisingListView,AdvertisingCreateView,AdvertisingUpdateView,AdvertisingDeleteView

from core.erp.views.galery import views
app_name = 'erp'

urlpatterns = [
    # category
    
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # test
    # client
    path('music/list/', MusicListView.as_view(), name='music_list'),
    path('music/add/', MusicCreateView.as_view(), name='music_create'),
    path('music/update/<int:pk>/', MusicUpdateView.as_view(), name='music_update'),
    path('music/delete/<int:pk>/', MusicDeleteView.as_view(), name='music_delete'),
   
     # live
    path('live/list/', LiveListView.as_view(), name='live_list'),
    path('live/add/', LiveCreateView.as_view(), name='live_create'),
    path('live/update/<int:pk>/', LiveUpdateView.as_view(), name='live_update'),
    path('live/delete/<int:pk>/', LiveDeleteView.as_view(), name='live_delete'),
    
     # PUBLICIDAD
    path('advertising/list/', AdvertisingListView.as_view(), name='advertising_list'),
    path('advertising/add/', AdvertisingCreateView.as_view(), name='advertising_create'),
    path('advertising/update/<int:pk>/', AdvertisingUpdateView.as_view(), name='advertising_update'),
    path('advertising/delete/<int:pk>/', AdvertisingDeleteView.as_view(), name='advertising_delete'),

    #GALERIA

    path('galery/list/', views.gallery , name='galery_list'),
    path('galery/add/', views.addPhoto, name='galery_create'),
    path('galery/delete/<int:post_id>', views.eliminar, name='galery_delete'),



    #GALERIA

    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

]
