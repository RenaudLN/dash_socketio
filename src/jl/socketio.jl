# AUTO GENERATED FILE - DO NOT EDIT

export socketio

"""
    socketio(;kwargs...)

A DashSocketIO component.
Socket.IO Dash component.
Keyword arguments:
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `connected` (Bool; optional): Whether the client is connected to the websocket - READONLY
- `eventNames` (Array of Strings; optional): Name of Socket.IO events to listen to
- `url` (String; optional): The socket.io server URL
"""
function socketio(; kwargs...)
        available_props = Symbol[:id, :connected, :eventNames, :url]
        wild_props = Symbol[]
        return Component("socketio", "DashSocketIO", "dash_socketio", available_props, wild_props; kwargs...)
end

