from django.conf.urls import url

from .views import(
     restaurant_listview,
     RestaurantListView,
     RestaurantDetailView,
     RestaurantCreateView
 )








urlpatterns = [
    url(r'^restaurants/create/$',RestaurantCreateView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view()),
    url(r'^restaurants/$',RestaurantListView.as_view()),
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]
