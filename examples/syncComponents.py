from dash_socketio import DashSocketIO
import dash_mantine_components as dmc
from dash import (
    Dash,
    Input,
    Output,
    callback,
    clientside_callback,
)
from flask_socketio import SocketIO, emit

app = Dash(__name__)
app.server.secret_key = "Test!"

socketio = SocketIO(app.server)

app.layout = dmc.NotificationsProvider(
    [
        dmc.Title("Hello Socket.IO!", mb="xl"),
        dmc.Text("Open a second tab or browser"),
        dmc.Stack(
            [
                dmc.Select(
                    label="Select framework",
                    placeholder="Select one",
                    id="framework-select",
                    value="Angular",
                    data=[
                        {"value": "React", "label": "React"},
                        {"value": "Angular", "label": "Angular"},
                        {"value": "Svelte", "label": "Svelte"},
                        {"value": "Vue", "label": "Vue"},
                    ],
                    style={"width": 200, "marginBottom": 10},
                ),
                dmc.Text(id="selected-value"),
            ],
            spacing="xs",
        ),
        DashSocketIO(id="socketio", eventNames=["select"]),
    ],
    position="bottom-right",
)


def align_framework(framework):
    # Be carfule, broadcast sents it to all the clients. Another way is using rooms.
    # This is in the documentation of Flask SocketIO
    emit("select", framework, namespace="/", broadcast=True)


@callback(Output("selected-value", "children"), Input("framework-select", "value"))
def select_value(value):
    align_framework(value)
    return value


clientside_callback(
    """(framework_new) => {
        if (!framework_new) return dash_clientside.no_update
        return framework_new
    }""",
    Output("framework-select", "value", allow_duplicate=True),
    Input("socketio", "data-select"),
    prevent_initial_call=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
