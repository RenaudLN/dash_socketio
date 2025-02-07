import json
from dash_socketio import DashSocketIO
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, _dash_renderer, callback, clientside_callback, html, no_update
from flask_socketio import SocketIO, emit
from plotly.io.json import to_json_plotly

_dash_renderer._set_react_version("18.3.1")
app = Dash(__name__, external_stylesheets=dmc.styles.ALL)
app.server.secret_key = "Test!"

socketio = SocketIO(app.server)

app.layout = dmc.MantineProvider(
    dmc.Container(
        [
            dmc.NotificationProvider(position="top-right"),
            dmc.Title("Hello Socket.IO!", mb="xl"),
            dmc.Stack(
                [
                    dmc.Textarea(id="msg", minRows=5, placeholder="Write something in the chat"),
                    html.Div(dmc.Button("Send", id="send", mb="md", disabled=True)),
                ],
                gap="xs",
            ),
            dmc.Stack([], id="chat-messages", style={"maxWidth": "60ch"}),
            DashSocketIO(id="socketio", eventNames=["chatMsg"]),
        ],
        p="1rem 2rem",
    ),
)


def jsonify_data(data):
    return json.loads(to_json_plotly(data))


@callback(
    Output("msg", "value"),
    Input("send", "n_clicks"),
    State("msg", "value"),
    State("socketio", "socketId"),
    running=[[Output("send", "loading"), True, False]],
    prevent_initial_call=True,
)
def display_status(send, msg, socket_id):
    if not send or not msg:
        return no_update
    emit(
        "chatMsg",
        jsonify_data(dmc.Paper(
            [
                dmc.Text(f"{socket_id} says", size="xs", c="dimmed", mb=4),
                dmc.Text(msg),
            ],
            p="0.5rem 1rem",
            withBorder=True,
        )),
        namespace="/",
        broadcast=True,
        # skip_sid=socket_id,
    )
    return ""

clientside_callback(
    """connected => !connected""",
    Output("send", "disabled"),
    Input("socketio", "connected"),
)

clientside_callback(
    """(msg, children) => !msg ? dash_clientside.no_update : [...children, msg]""",
    Output("chat-messages", "children"),
    Input("socketio", "data-chatMsg"),
    State("chat-messages", "children"),
    prevent_initial_call=True,
)


if __name__ == '__main__':
    app.run_server(debug=True)
