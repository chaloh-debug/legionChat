# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message

@login_required
def index(request):
    room_names = ChatRoom.objects.all()
    return render(request, "chat/index.html", {"room_names": room_names})


@login_required
def room(request, slug):
    room_names = ChatRoom.objects.all()
    room = ChatRoom.objects.get(slug=slug)
    return render(request, "chat/room.html", {"room_names": room_names, "room": room})
