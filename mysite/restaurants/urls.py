from django.conf.urls import url

from .views import(
     restaurant_listview,
     RestaurantListView,
 )








urlpatterns = [
    url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view() ),
    url(r'^',restaurant_listview,name="list" ),
]
