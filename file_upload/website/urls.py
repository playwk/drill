from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^moment_input', views.moment_input),
    url(r'^welcome', views.welcome, name='welcome'),
]