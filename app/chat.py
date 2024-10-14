import socketio
from fastapi import FastAPI

from .models import Message, User, Room
from .db import get_db


sio = socketio.AsyncServer(async_mode="asgi")
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)


@sio.event
async def connect(sid, environ):
    print(f"User {sid} connected")
    await sio.emit("message", {"msg": "Welcome!"}, to=sid)


@sio.event
async def join_room(sid, data):
    room_name = data["room"]
    sio.enter_room(sid, room_name)
    await sio.emit("message", {"msg": f"User joined room {room_name}"}, to=room_name)


@sio.event
async def send_message(sid, data):
    room = data["room"]
    message = data["msg"]
    await sio.emit("message", {"msg": message}, to=room)
    db = get_db()
    new_message = Message(content=message, user_id=sid, room_id=room)
    db.add(new_message)
    db.commit()


@sio.event
async def disconnect(sid):
    print(f"User {sid} disconnected")
