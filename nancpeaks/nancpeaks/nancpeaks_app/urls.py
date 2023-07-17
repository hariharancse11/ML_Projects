from django.urls import path
from . import views
urlpatterns = [
    path('',views.to_speech, name='to_speech')
]
