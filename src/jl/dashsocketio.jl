# AUTO GENERATED FILE - DO NOT EDIT

export dashsocketio

"""
    dashsocketio(;kwargs...)

A DashSocketIO component.

Keyword arguments:
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `debug` (Bool; optional)
- `send` (Dict; optional)
- `url` (String; required)
"""
function dashsocketio(; kwargs...)
        available_props = Symbol[:id, :debug, :send, :url]
        wild_props = Symbol[]
        return Component("dashsocketio", "DashSocketIO", "dash_socketio", available_props, wild_props; kwargs...)
end

