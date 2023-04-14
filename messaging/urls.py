from django.urls import path
from . import views
from messaging.views import compose_message

app_name = 'messaging'


urlpatterns = [
    path('compose/<int:recipient_id>/', compose_message,
         name='compose_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('<int:message_id>/', views.message_detail, name='message_detail'),
]
