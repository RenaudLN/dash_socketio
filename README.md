# Dash Socketio

This package integration of the [Flask SocketIO](https://flask-socketio.readthedocs.io/en/latest/) into Dash.
Flask SocketIO provides the server side capabilities of pushing data to clients while Dash SocketIO enables the Dashboard to recieve and process the messages.

## Install

```shell
pip install dash_socketio
```
## Use Cases:
There are several potential usecases which Dash SocketIO enables:
1. Send update messages while a callback is processing e.g. streaming responeses or downloading data
2. Sending messages to multiple users at once and accross clients e.g. chat applications
3. Align data or filters for the same user accross clients.

## Demo and Quickstart

!ToDo: Add gif here

```
import time
import uuid
from dash_socketio import DashSocketIO
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback, clientside_callback, html, no_update
from flask_socketio import SocketIO, emit

app = Dash(__name__)
app.server.secret_key = "Test!"

socketio = SocketIO(app.server)

app.layout = dmc.NotificationsProvider(
    [
        dmc.Title("Hello Socket.IO!", mb="xl"),
        dmc.Stack(
            [
                dmc.Textarea(id="dummy", minRows=5, placeholder="Ask LoremLM something..."),
                html.Div(dmc.Button("Ask LoremLM", id="btn", mb="md", disabled=True)),
            ]
        ),
        dmc.Text(id="results", style={"maxWidth": "60ch"}),
        html.Div(id="notification_wrapper"),
        DashSocketIO(id='socketio', eventNames=["notification", "stream"]),
    ],
    position="bottom-right",
)


@socketio.on("connect")
def on_connect():
    print("Client connected")

@socketio.on("disconnect")
def on_disconnect():
    print("Client disconnected")

def notify(socket_id, message, color=None):
    emit(
        "notification",
        dmc.Notification(
            message=message,
            action="show",
            id=uuid.uuid4().hex,
            color=color,
        ).to_plotly_json(),
        namespace="/",
        to=socket_id,
    )

paragraph = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Integer augue eros, tincidunt vitae eros eu, faucibus tempus risus.
Donec ullamcorper velit in arcu fermentum faucibus.
Etiam finibus tortor ac vestibulum dictum. Vestibulum ultricies risus eu lacus luctus pretium.
Duis congue et nisl eu fringilla. Mauris lorem metus, varius eget ex eget, ultrices suscipit est.
Integer nunc risus, auctor posuere vehicula id, rutrum et urna.
Pellentesque gravida, orci id pharetra tempus, nulla neque sagittis elit, condimentum tempor mi velit et urna.
Fusce faucibus ac libero facilisis commodo. Quisque condimentum suscipit mi.
Vivamus augue neque, commodo sagittis mollis sed, mollis in sapien.
Integer cursus et magna nec cursus.
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
"""

@callback(
    Output("results", "children"),
    Output("notification_wrapper", "children", allow_duplicate=True),
    Input("btn", "n_clicks"),
    State("socketio", "socketId"),
    running=[[Output("results", "children"), "", None]],
    prevent_initial_call=True,
)
def display_status(n_clicks, socket_id):
    if not n_clicks or not socket_id:
        return no_update, []
    notify(socket_id, "Sending the question to LoremLM...")
    time.sleep(1)
    notify(socket_id, "Streaming answer...")

    for i, word in enumerate(paragraph.replace("\n", " ").split(" ")):
        emit("stream", " " * bool(i) + word, namespace="/", to=socket_id)
        time.sleep(0.05)

    notify(socket_id, "Done!", color="green")

    return paragraph, []

clientside_callback(
    """connected => !connected""",
    Output("btn", "disabled"),
    Input("socketio", "connected"),
)

clientside_callback(
    """(notification) => {
        if (!notification) return dash_clientside.no_update
        return notification
    }""",
    Output("notification_wrapper", "children", allow_duplicate=True),
    Input("socketio", "data-notification"),
    prevent_initial_call=True,
)

clientside_callback(
    """(word, text) => text + word""",
    Output("results", "children", allow_duplicate=True),
    Input("socketio", "data-stream"),
    State("results", "children"),
    prevent_initial_call=True,
)


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)
```

## SocketIO Reference

```
- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- connected (boolean; optional):
    Whether the client is connected to the websocket - READONLY.

- eventNames (list of strings; optional):
    Name of Socket.IO events to listen to.

- socketId (string; optional):
    The socket ID.

- url (string; optional):
    The socket.io server URL."""

```

## Development
### Getting Started

1. Create a new python environment:
   ```shell
   python -m venv venv
   . venv/bin/activate
   ```
   _Note: venv\Scripts\activate for windows_

2. Install python dependencies:
   ```shell
   pip install -r requirements.txt
   ```
3. Install npm packages:
   1. Optional: use [nvm](https://github.com/nvm-sh/nvm) to manage node version:
      ```shell
      nvm install
      nvm use
      ```
   2. Install:
      ```shell
      npm install
      ```
4. Build:
   ```shell
   npm run build
   ```

### Component Code

### Publish

If publish on npm:
```shell
npm build
npm publish
```

### Justfile

Alternatively, use the provided [just](https://github.com/casey/just) commands:

1. Create a Python environment from previous step 1 and install:
   ```shell
   just install
   ```
2. Build
   ```shell
   just build
   ```
3. Publish
   ```shell
   just publish
   ```
4. See all commands with `just -l`
