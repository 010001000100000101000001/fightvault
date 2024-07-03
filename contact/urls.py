from django.urls import path
from .views import contact_view, send_email_view, thank_you_view

urlpatterns = [
    path('', contact_view, name='contact'),
    path('send-email/', send_email_view, name='send_email'),
    path('thank_you/', thank_you_view, name='thank_you')
]
