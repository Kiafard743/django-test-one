from django.urls import path
from message.viewss import Messageview

urlpatterns = [
path('', Messageview.as_view(), name='message')
]