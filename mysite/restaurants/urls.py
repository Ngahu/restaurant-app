from django.conf.urls import url

from .views import(
     restaurant_listview,
     RestaurantListView,
     RestaurantDetailView,
     RestaurantCreateView,
     about,
     home
 )








urlpatterns = [
    url(r'^create/$',RestaurantCreateView.as_view(),name='restaurants-create'),
    url(r'^about/$',about,name='about'),
    url(r'^$',home,name='home'),
    url(r'^restaurants/$',RestaurantListView.as_view(),name='restaurants'),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view(),name='restaurant-detail'),
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]
