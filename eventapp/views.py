from django.shortcuts import render
from .models import Event, Room, Booth

def event_view(request, event_id):
    event = Event.objects.get(id=event_id)
    rooms = Room.objects.filter(event=event)
    return render(request, 'event.html', {'event': event, 'rooms': rooms})

def room_view(request, room_id):
    room = Room.objects.get(id=room_id)
    booths = Booth.objects.filter(room=room)
    return render(request, 'room.html', {'room': room, 'booths': booths})
