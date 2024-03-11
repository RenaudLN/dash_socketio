import time
import uuid
from dash_socketio import DashSocketIO
import dash_mantine_components as dmc
from dash import ALL, Dash, Input, Output, State, callback, clientside_callback, ctx, html, no_update
from flask import session
from flask_socketio import SocketIO, emit, join_room

app = Dash(__name__)
app.server.secret_key = "Test!"

socketio = SocketIO(app.server)

app.layout = dmc.NotificationsProvider(
    [
        dmc.Title("Hello Socket.IO!", mb="xl"),
        dmc.Group(
            [
                dmc.TextInput(id={"type": "control", "id": "name"}, debounce=500, label="Name"),
                dmc.Select(data=["Montreal", "NYC", "Paris"], id={"type": "control", "id": "city"}, label="City"),
                dmc.SegmentedControl(data=["Male", "Female"], id={"type": "control", "id": "gender"}),
            ],
            align="end",
        ),
        html.Div(id="dummy"),
        DashSocketIO(id='socketio', eventNames=["syncControl"]),
    ],
    position="bottom-right",
)

@app.server.before_request
def add_session_id():
    if "session_id" not in session:
        session["session_id"] = uuid.uuid4().hex


@socketio.on("connect")
def join_session_id_room():
    session_id = session["session_id"]
    join_room(session_id)


@callback(
    Output("dummy", "data-noOutput"),
    Input({"type": "control", "id": ALL}, "value"),
    State("socketio", "socketId")
)
def sync_controls(controls, socket_id):
    if not ctx.triggered_id or not any(controls):
        return no_update

    emit(
        "syncControl",
        {
            "control_id": ctx.triggered_id["id"],
            "value": ctx.triggered[0]["value"],
        },
        to=session["session_id"],
        skip_sid=socket_id,
        namespace="/",
    )
    return no_update


clientside_callback(
    """(data, ids, current) => {
        if (!data) return Array(ids.length).fill(dash_clientside.no_update)
        const idxToChange = ids.map((x, i) => [x.id, i]).filter(y => y[0] === data.control_id)[0][1]
        return current.slice(0, idxToChange).concat([data.value]).concat(current.slice(idxToChange + 1))
    }""",
    Output({"type": "control", "id": ALL}, "value"),
    Input("socketio", "data-syncControl"),
    State({"type": "control", "id": ALL}, "id"),
    State({"type": "control", "id": ALL}, "value"),
    prevent_initial_call=True,
)


if __name__ == '__main__':
    app.run_server(debug=True)
