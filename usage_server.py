from collections import defaultdict
from enum import Enum

from flask import Flask, request
from flask_socketio import SocketIO
from flask_socketio import emit as socketio_emit
from flask_socketio import join_room, leave_room
from loguru import logger

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:8050")


class CommonRoom(str, Enum):
    Slytherin = "Slytherin"
    Gryffindor = "Gryffindor"
    Hufflepuff = "Hufflepuff"
    Ravenclaw = "Ravenclaw"


HISTORY = defaultdict(list)
USER_TO_ROOM: dict[str:CommonRoom] = {}


_SOCKETIO_EVENT = "ws-event"


def emit(event: str, data: dict, **kwargs) -> None:
    logger.info(f"Sending {data=} to {event=}")
    socketio_emit(_SOCKETIO_EVENT, {event: data}, **kwargs)


@socketio.on("connect")
def handle_connect():
    sid = request.sid
    logger.info(f"Client connected with sid {sid}")


@socketio.on("disconnect")
def handle_disconnect():
    sid = request.sid
    room = USER_TO_ROOM.pop(sid, None)
    if room:
        leave_room(room, sid=sid)
        logger.info(f"User {sid} disconnected")
    else:
        logger.info(f"Unkown user with sid {sid} disconnected")


@socketio.on("available_rooms")
def handle_available_rooms():
    logger.debug("available_rooms triggered")
    emit("rooms", [room.value for room in CommonRoom])


@socketio.on("join_room")
def handle_join_room(data):
    logger.debug("join_room triggered")

    if (room := data["room"]) not in CommonRoom:
        raise ValueError(f"Invalid room {room}")

    sid = request.sid
    if current_room := USER_TO_ROOM.get(sid):
        leave_room(current_room, sid=sid)
        logger.info(f"User {sid} left room {current_room}")

    join_room(room, sid=sid)
    logger.info(f"User {sid} joined room {room}")

    USER_TO_ROOM[sid] = room
    emit("room_joined", HISTORY[room])


@socketio.on("send_message")
def handle_send_message(message):
    logger.debug("send_message triggered")

    sid = request.sid
    room = USER_TO_ROOM[sid]

    logger.info(f"User {sid} sent message in {room=}")

    HISTORY[room].append({"from": sid, "message": message})

    emit("new_message", {"from": sid, "message": message}, room=room)


if __name__ == "__main__":
    socketio.run(app)
