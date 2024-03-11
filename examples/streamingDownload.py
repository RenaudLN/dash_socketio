import io
import time
import uuid
from dash_socketio import DashSocketIO
import dash_mantine_components as dmc
from dash import (
    Dash,
    Input,
    Output,
    State,
    callback,
    clientside_callback,
    html,
    no_update,
    dcc,
)
from flask_socketio import SocketIO, emit
import base64

app = Dash(__name__)
app.server.secret_key = "Test!"

socketio = SocketIO(app.server)

app.layout = dmc.NotificationsProvider(
    [
        dmc.Title("Hello Socket.IO!", mb="xl"),
        dmc.Stack(
            [
                dmc.Textarea(
                    id="dummy", minRows=5, placeholder="Ask LoremLM something..."
                ),
                html.Div(dmc.Button("Ask LoremLM", id="btn", mb="md", disabled=True)),
            ]
        ),
        dmc.Text(id="results", style={"maxWidth": "60ch"}),
        html.Button(id="trigger_download", style={"display": "none"}),
        html.Div(id="notification_wrapper"),
        DashSocketIO(id="socketio", eventNames=["notification", "stream"]),
        dcc.Download(id="download"),
        dcc.Store(id="download_data", storage_type="memory", data=""),
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


def split_base64_to_chunks(base64_string, num_chunks):
    # Calculate the chunk size
    chunk_size = len(base64_string) // (num_chunks - 1)

    # Split the bytes into chunks
    chunks = [
        base64_string[i * chunk_size : (i + 1) * chunk_size] for i in range(num_chunks)
    ]

    return chunks


app.clientside_callback(
    """(n, data) => {console.log(data); return [{base64: true, content: data, filename: 'test.txt'}, '']}""",
    Output("download", "data"),
    Output("download_data", "data", allow_duplicate=True),
    Input("trigger_download", "n_clicks"),
    State("download_data", "data"),
    prevent_initial_call=True,
)


@callback(
    Output("trigger_download", "n_clicks"),
    Output("notification_wrapper", "children", allow_duplicate=True),
    Output("results", "children"),
    Input("btn", "n_clicks"),
    State("socketio", "socketId"),
    State("trigger_download", "n_clicks"),
    running=[[Output("results", "children"), "", None]],
    prevent_initial_call=True,
)
def display_status(n_clicks, socket_id, clicks):
    if not n_clicks or not socket_id:
        return no_update, []
    notify(socket_id, "Processing download...")
    time.sleep(1)
    notify(socket_id, "Downloading...")

    stream = io.BytesIO(paragraph.encode("utf-8"))

    # Read the stream content into a byte array
    stream.seek(0)  # Reset the stream position
    content_bytes = stream.read()
    base64_string = base64.b64encode(content_bytes).decode("utf-8")
    # Split into 10 chunks
    num_chunks = 10
    chunk_list = split_base64_to_chunks(base64_string, num_chunks)

    # Print each chunk
    for i, chunk in enumerate(chunk_list):
        print(f"Chunk {i + 1}: {chunk}")
        emit("stream", chunk, namespace="/", to=socket_id)
        notify(socket_id, f"{(i + 1)/num_chunks*100}% downloaded")
        time.sleep(1)

    notify(socket_id, "Done!", color="green")

    return (clicks or 0) + 1, [], paragraph


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
    """(newData, prevData) => (prevData || '') + newData""",
    Output("download_data", "data", allow_duplicate=True),
    Input("socketio", "data-stream"),
    State("download_data", "data"),
    prevent_initial_call=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
