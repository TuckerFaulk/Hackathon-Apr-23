from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('compose/<int:recipient_id>/',
         views.compose_message, name='compose_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('messages/<int:message_id>/', views.message_detail,
         name='message_detail'),
    path('reply/<int:message_id>/', views.reply_message, name='reply_message'),
]
