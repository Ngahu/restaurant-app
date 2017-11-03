from django.conf.urls import url

from .views import(
    restaurant_listview
)


urlpatterns = [
    url(r'^',restaurant_listview,name="list" ),
]
