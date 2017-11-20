from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^u/',include('profiles.urls', namespace='Profiles')),
    url(r'^restaurants/',include('restaurants.urls', namespace='Restaurant')),
    url(r'^accounts/',include('accounts.urls', namespace='Accounts')),
    url(r'^menus/',include('menus.urls', namespace='Menus')),

]
