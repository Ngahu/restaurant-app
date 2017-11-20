from django.conf.urls import url

from .views import(
     RestaurantListView,
     RestaurantDetailView,
     RestaurantCreateView,
     RestaurantUpdateView,
     about,
     home
 )








urlpatterns = [
    url(r'^create/$',RestaurantCreateView.as_view(),name='restaurants-create'),
    url(r'^about/$',about,name='about'),
    url(r'^$',home,name='home'),
    url(r'^restaurants/$',RestaurantListView.as_view(),name='list'),
    #url(r'^(?P<slug>[\w-]+)/edit/$',RestaurantUpdateView.as_view(),name='update'),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantUpdateView.as_view(),name='restaurant-detail'),
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]
