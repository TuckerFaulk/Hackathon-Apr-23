from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.models import User
from .models import Message
from .forms import ComposeMessageForm, ReplyMessageForm


@login_required
def compose_message(request):
    recipient_id = request.GET.get('recipient_id')
    recipient = get_object_or_404(User, id=recipient_id) if recipient_id else None
    if request.method == 'POST':
        form = ComposeMessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            new_message = Message(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                message=message,
            )
            new_message.save()
            messages.success(request, 'Message sent successfully')
            return redirect(reverse('messaging:inbox'))
    else:
        form = ComposeMessageForm()
    return render(
        request,
        'messaging/compose_message.html',
        {'form': form, 'recipient': recipient}
    )


@login_required
def inbox(request):
    message_list = Message.objects.filter(recipient=request.user)
    return render(request, 'messaging/inbox.html',
                  {'message_list': message_list})


@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    if request.method == 'POST':
        form = ReplyMessageForm(request.POST)
        if form.is_valid():
            subject = 'RE: ' + message.subject
            reply_message = Message(
                sender=request.user,
                recipient=message.sender,
                subject=subject,
                message=form.cleaned_data['message'],
            )
            reply_message.save()
            message.read = True
            message.save()
            return redirect('messaging:inbox')
    else:
        form = ReplyMessageForm()
    return render(request, 'messaging/message_detail.html',
                  {'message': message, 'form': form})


@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent_messages.html',
                  {'messages': messages})
