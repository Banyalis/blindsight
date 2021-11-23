from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/auth/', views.user_login_api, name='login'),
]
