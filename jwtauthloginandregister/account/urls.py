from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from .views import POSTView
urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('POST/', POSTView.as_view(), name='post')
]