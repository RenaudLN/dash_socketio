# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSocketIO(Component):
    """A DashSocketIO component.
Socket.IO Dash component.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- connected (boolean; optional):
    Whether the client is connected to the websocket - READONLY.

- eventNames (list of strings; optional):
    Name of Socket.IO events to listen to.

- socketId (string; optional):
    The socket ID.

- url (string; optional):
    The socket.io namespace url, defaults to window.location.origin."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_socketio'
    _type = 'DashSocketIO'
    @_explicitize_args
    def __init__(self, url=Component.UNDEFINED, eventNames=Component.UNDEFINED, connected=Component.UNDEFINED, socketId=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'connected', 'eventNames', 'socketId', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'connected', 'eventNames', 'socketId', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashSocketIO, self).__init__(**args)
