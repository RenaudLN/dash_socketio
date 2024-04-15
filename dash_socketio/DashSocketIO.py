# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSocketIO(Component):
    """A DashSocketIO component.


Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- debug (boolean; optional)

- send (dict; optional)

- url (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_socketio'
    _type = 'DashSocketIO'
    @_explicitize_args
    def __init__(self, url=Component.REQUIRED, debug=Component.UNDEFINED, send=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'debug', 'send', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'debug', 'send', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashSocketIO, self).__init__(**args)
