# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from datetime import datetime
from time import strftime

@login_required
def index(request):
    room_names = ChatRoom.objects.all()
    return render(request, "chat/index.html", {"room_names": room_names})


@login_required
def room(request, slug):
    time = datetime.now()
    # time = time.strftime("%I:%M")
    room_names = ChatRoom.objects.all()
    room = ChatRoom.objects.get(slug=slug)

    messages = Message.objects.filter(room=room)[0:25]
    sender = Message.objects.filter

    return render(request, "chat/room.html", {"room_names": room_names, "room": room, "time": time, "messages": messages})
