import uuid
from typing import Any

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, html
from dash.exceptions import PreventUpdate
from loguru import logger

from dash_socketio import DashSocketIO


def websocket_request(
    event: str,
    data: Any = None,
):
    """
    Simple helper function to create a websocket request.

    This is required because we need to alter the "send" property of the
    DashSocketIO component so we had a uuid to each request.
    Otherwise, if we requested two identical events in a row, the second
    request would be ignored.

    :param event: The event to send
    :param data: The data to send with the event. Defaults to None. Usually a dict.
    :return: A dictionary with the event, data, and a uuid.
    """
    return {
        "event": event,
        "data": data,
        "id": str(uuid.uuid4()),
    }


app = Dash(__name__)

base_url = "ws://localhost:5000"

app.layout = html.Div(
    children=[
        DashSocketIO(
            id="websocket",
            url=base_url,
        ),
        dmc.RadioGroup(
            id="common-room",
            value=None,
            label="Select a Common Room to join",
            style={"marginBottom": "10px"},
        ),
        html.Div(
            id="chat-text",
            style={
                "height": "50vh",
                "width": "90vw",
                "border": "1px solid black",
                "overflow": "auto",
            },
        ),
        dbc.Input(
            id="chat-input",
            placeholder="Type your message here",
            style={"width": "90vw"},
            disabled=True,
        ),
    ],
    style={
        "display": "flex",
        "flex-direction": "column",
        "align-items": "center",
        "justify-content": "center",
        "height": "98vh",
    },
)


def _format_message(message: dict) -> html.Div:
    return html.Div(
        [
            dmc.Text(f"{message['from']} : ", color="blue"),
            dmc.Space(w=10),
            dmc.Text(message["message"]),
        ],
        style={"display": "flex", "flex-direction": "row"},
    )


@app.callback(
    Output("websocket", "send", allow_duplicate=True),
    Input("websocket", "id"),
    prevent_initial_call="initial",
)
def fetch_rooms(_):
    logger.debug("Requesting available rooms")
    return websocket_request("available_rooms")


@app.callback(
    Output("common-room", "children"),
    Input("websocket", "data-rooms"),
    prevent_initial_call=True,
)
def present_rooms(rooms):
    logger.debug(f"Updating rooms: {rooms}")
    return [dmc.Radio(label=room, value=room) for room in rooms]


@app.callback(
    Output("websocket", "send", allow_duplicate=True),
    Input("common-room", "value"),
    prevent_initial_call=True,
)
def join_room(room):
    logger.debug(f"Joining room {room}")
    return websocket_request("join_room", {"room": room})


@app.callback(
    Output("chat-text", "children"),
    Input("websocket", "data-room_joined"),
    prevent_initial_call=True,
)
def show_chat_history(history):
    logger.debug("Updating chat text")
    return [_format_message(message) for message in history]


@app.callback(
    Output("websocket", "send", allow_duplicate=True),
    Output("chat-input", "value"),
    Input("chat-input", "n_submit"),
    State("chat-input", "value"),
    prevent_initial_call=True,
)
def send_message(_, message):
    if not message:
        raise PreventUpdate

    logger.debug("Sending message")
    return websocket_request("send_message", message), None


@app.callback(
    Output("chat-text", "children", allow_duplicate=True),
    Input("websocket", "data-new_message"),
    State("chat-text", "children"),
    prevent_initial_call=True,
)
def update_chat_text(new_message, chat_text):
    logger.debug("Updating chat text")
    chat_text.append(_format_message(new_message))
    return chat_text


# Enable the chat-text input if the user is in a room
app.clientside_callback(
    """
    function (room) {
        return room === null;
    }
    """,
    Output("chat-input", "disabled"),
    Input("common-room", "value"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run_server(debug=False)
