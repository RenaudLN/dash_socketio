# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSocketIO(Component):
    """A DashSocketIO component.


Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- autoConnect (boolean; default True):
    Whether to automatically connect on component mount.

- connected (boolean; default False):
    Whether the client is connected to the websocket - READONLY.

- eventNames (list of strings; optional):
    Name of Socket.IO events to listen to.

- hasError (boolean; default False):
    Whether socket has failed to connect - READONLY.

- lastError (dict; optional):
    Last error encountered - READONLY.

    `lastError` is a dict with keys:

    - name (string; required)

    - message (string; required)

    - stack (string; optional)

- path (string; default '/socket.io'):
    The path for the Socket.IO endpoint, defaults to '/socket.io'.

- reconnection (boolean; default True):
    Whether to enable reconnection.

- reconnectionAttempts (number; default Infinity):
    Number of reconnection attempts before giving up.

- reconnectionDelay (number; default 1000):
    Initial delay in milliseconds before reconnection attempt.

- reconnectionDelayMax (number; default 5000):
    Maximum delay in milliseconds between reconnection attempts.

- socketId (string; optional):
    The socket ID - READONLY.

- socketOptions (dict; optional):
    Additional Socket.IO options.

    `socketOptions` is a dict with keys:

    - forceNew (boolean; optional):
        Should we force a new Manager for this connection?
        @,default,False.

    - multiplex (boolean; optional):
        Should we multiplex our connection (reuse existing Manager) ?
        @,default,True.

    - path (string; optional):
        The path to get our client file from, in the case of the
        server serving it @,default,'/socket.io'.

    - reconnection (boolean; optional):
        Should we allow reconnections? @,default,True.

    - reconnectionAttempts (number; optional):
        How many reconnection attempts should we try?
        @,default,Infinity.

    - reconnectionDelay (number; optional):
        The time delay in milliseconds between reconnection attempts
        @,default,1000.

    - reconnectionDelayMax (number; optional):
        The max time delay in milliseconds between reconnection
        attempts @,default,5000.

    - randomizationFactor (number; optional):
        Used in the exponential backoff jitter when reconnecting
        @,default,0.5.

    - timeout (number; optional):
        The timeout in milliseconds for our connection attempt
        @,default,20000.

    - autoConnect (boolean; optional):
        Should we automatically connect? @,default,True.

    - parser (boolean | number | string | dict | list; optional):
        the parser to use. Defaults to an instance of the Parser that
        ships with socket.io.

    - host (string; optional):
        The host that we're connecting to. Set from the URI passed
        when connecting.

    - hostname (string; optional):
        The hostname for our connection. Set from the URI passed when
        connecting.

    - secure (boolean; optional):
        If this is a secure connection. Set from the URI passed when
        connecting.

    - port (string | number; optional):
        The port for our connection. Set from the URI passed when
        connecting.

    - query (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
        Any query parameters in our uri. Set from the URI passed when
        connecting.

    - agent (string; optional):
        `http.Agent` to use, defaults to `False` (NodeJS only)  Note:
        the type should be \"undefined | http.Agent | https.Agent |
        False\", but this would break browser-only clients.
        @,see,https,://nodejs.org/api/http.html#httprequestoptions-callback.

    - upgrade (boolean; optional):
        Whether the client should try to upgrade the transport from
        long-polling to something better. @,default,True.

    - forceBase64 (boolean; optional):
        Forces base 64 encoding for polling transport even when XHR2
        responseType is available and WebSocket even if the used
        standard supports binary.

    - timestampParam (string; optional):
        The param name to use as our timestamp key @,default,'t'.

    - timestampRequests (boolean; optional):
        Whether to add the timestamp with each transport request.
        Note: this is ignored if the browser is IE or Android, in
        which case requests are always stamped @,default,False.

    - transports (list of strings; optional):
        A list of transports to try (in order). Engine.io always
        attempts to connect directly with the first one, provided the
        feature detection test for it passes.
        @,default,['polling','websocket', 'webtransport'].

    - rememberUpgrade (boolean; optional):
        If True and if the previous websocket connection to the server
        succeeded, the connection attempt will bypass the normal
        upgrade process and will initially try websocket. A connection
        attempt following a transport error will use the normal
        upgrade process. It is recommended you turn this on only when
        using SSL/TLS connections, or if you know that your network
        does not block websockets. @,default,False.

    - onlyBinaryUpgrades (boolean; optional):
        Are we only interested in transports that support binary?.

    - requestTimeout (number; optional):
        Timeout for xhr-polling requests in milliseconds (0) (only for
        polling transport).

    - transportOptions (dict; optional):
        Transport options for Node.js client (headers etc).

        `transportOptions` is a dict with keys:

        - constructor (optional):
            The initial value of Object.prototype.constructor is the
            standard built-in Object constructor.

        - toString (optional):
            Returns a string representation of an object.

        - toLocaleString (optional):
            Returns a date converted to a string using the current
            locale.

        - valueOf (optional):
            Returns the primitive value of the specified object.

        - hasOwnProperty (optional):
            Determines whether an object has a property with the
            specified name. @,param,v, ,A property name.

        - isPrototypeOf (optional):
            Determines whether an object exists in another object's
            prototype chain. @,param,v, ,Another object whose
            prototype chain is to be checked.

        - propertyIsEnumerable (optional):
            Determines whether a specified property is enumerable.
            @,param,v, ,A property name.

    - pfx (string; optional):
        (SSL) Certificate, Private key and CA certificates to use for
        SSL. Can be used in Node.js client environment to manually
        specify certificate information.

    - key (string; optional):
        (SSL) Private key to use for SSL. Can be used in Node.js
        client environment to manually specify certificate
        information.

    - passphrase (string; optional):
        (SSL) A string or passphrase for the private key or pfx. Can
        be used in Node.js client environment to manually specify
        certificate information.

    - cert (string; optional):
        (SSL) Public x509 certificate to use. Can be used in Node.js
        client environment to manually specify certificate
        information.

    - ca (string | list of strings; optional):
        (SSL) An authority certificate or array of authority
        certificates to check the remote host against.. Can be used in
        Node.js client environment to manually specify certificate
        information.

    - ciphers (string; optional):
        (SSL) A string describing the ciphers to use or exclude.
        Consult the [cipher format list]
        (http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT)
        for details on the format.. Can be used in Node.js client
        environment to manually specify certificate information.

    - rejectUnauthorized (boolean; optional):
        (SSL) If True, the server certificate is verified against the
        list of supplied CAs. An 'error' event is emitted if
        verification fails. Verification happens at the connection
        level, before the HTTP request is sent. Can be used in Node.js
        client environment to manually specify certificate
        information.

    - extraHeaders (dict with strings as keys and values of type string; optional):
        Headers that will be passed for each request to the server
        (via xhr-polling and via websockets). These values then can be
        used during handshake or for special proxies.

    - withCredentials (boolean; optional):
        Whether to include credentials (cookies, authorization
        headers, TLS client certificates, etc.) with cross-origin XHR
        polling requests @,default,False.

    - closeOnBeforeunload (boolean; optional):
        Whether to automatically close the connection whenever the
        beforeunload event is received. @,default,False.

    - useNativeTimers (boolean; optional):
        Whether to always use the native timeouts. This allows the
        client to reconnect when the native timeout functions are
        overridden, such as when mock clocks are installed.
        @,default,False.

    - autoUnref (boolean; optional):
        weather we should unref the reconnect timer when it is create
        automatically @,default,False.

    - perMessageDeflate (dict; optional):
        parameters of the WebSocket permessage-deflate extension (see
        ws module api docs). Set to False to disable. @,default,False.

        `perMessageDeflate` is a dict with keys:

        - threshold (number; required)

    - addTrailingSlash (boolean; optional):
        Whether we should add a trailing slash to the request path.
        @,default,True.

    - protocols (string | list of strings; optional):
        Either a single protocol string or an array of protocol
        strings. These strings are used to indicate sub-protocols, so
        that a single server can implement multiple WebSocket
        sub-protocols (for example, you might want one server to be
        able to handle different types of interactions depending on
        the specified protocol) @,default,[].

    - auth (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
        the authentication payload sent when connecting to the
        Namespace.

    - retries (number; optional):
        The maximum number of retries. Above the limit, the packet
        will be discarded.  Using `Infinity` means the delivery
        guarantee is \"at-least-once\" (instead of \"at-most-once\" by
        default), but a smaller value like 10 should be sufficient in
        practice.

    - ackTimeout (number; optional):
        The default timeout in milliseconds used when waiting for an
        acknowledgement.

- timeout (number; default 5000):
    Timeout in milliseconds for emitted events (0 means no timeout).

- url (string; optional):
    The socket.io server URL, defaults to window.location.origin."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_socketio'
    _type = 'DashSocketIO'
    @_explicitize_args
    def __init__(self, url=Component.UNDEFINED, path=Component.UNDEFINED, eventNames=Component.UNDEFINED, connected=Component.UNDEFINED, socketId=Component.UNDEFINED, autoConnect=Component.UNDEFINED, timeout=Component.UNDEFINED, reconnectionAttempts=Component.UNDEFINED, reconnectionDelay=Component.UNDEFINED, reconnectionDelayMax=Component.UNDEFINED, reconnection=Component.UNDEFINED, socketOptions=Component.UNDEFINED, lastError=Component.UNDEFINED, hasError=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoConnect', 'connected', 'eventNames', 'hasError', 'lastError', 'path', 'reconnection', 'reconnectionAttempts', 'reconnectionDelay', 'reconnectionDelayMax', 'socketId', 'socketOptions', 'timeout', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoConnect', 'connected', 'eventNames', 'hasError', 'lastError', 'path', 'reconnection', 'reconnectionAttempts', 'reconnectionDelay', 'reconnectionDelayMax', 'socketId', 'socketOptions', 'timeout', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashSocketIO, self).__init__(**args)
