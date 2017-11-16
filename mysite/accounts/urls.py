from django.conf.urls import url

from django.contrib.auth.views import LoginView




urlpatterns = [
    url(r'^accounts/login/$',LoginView.as_view(),name='login'),
]