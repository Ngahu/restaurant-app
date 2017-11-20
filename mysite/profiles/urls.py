from django.conf.urls import url

from .views import(
    ProfileDetailView
)


urlpatterns = [
    url(r'^(?P<full_name>[\w-]+)/$',ProfileDetailView.as_view(),name='detail'),  #full_name

]