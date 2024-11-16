# AUTO GENERATED FILE - DO NOT EDIT

export dashsocketio

"""
    dashsocketio(;kwargs...)

A DashSocketIO component.

Keyword arguments:
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `autoConnect` (Bool; optional): Whether to automatically connect on component mount
- `connected` (Bool; optional): Whether the client is connected to the websocket - READONLY
- `eventNames` (Array of Strings; optional): Name of Socket.IO events to listen to
- `hasError` (Bool; optional): Whether socket has failed to connect - READONLY
- `lastError` (optional): Last error encountered - READONLY. lastError has the following type: lists containing elements 'name', 'message', 'stack'.
Those elements have the following types:
  - `name` (String; required)
  - `message` (String; required)
  - `stack` (String; optional)
- `path` (String; optional): The path for the Socket.IO endpoint, defaults to '/socket.io'
- `reconnection` (Bool; optional): Whether to enable reconnection
- `reconnectionAttempts` (Real; optional): Number of reconnection attempts before giving up
- `reconnectionDelay` (Real; optional): Initial delay in milliseconds before reconnection attempt
- `reconnectionDelayMax` (Real; optional): Maximum delay in milliseconds between reconnection attempts
- `socketId` (String; optional): The socket ID - READONLY
- `socketOptions` (optional): Additional Socket.IO options. socketOptions has the following type: lists containing elements 'forceNew', 'multiplex', 'path', 'reconnection', 'reconnectionAttempts', 'reconnectionDelay', 'reconnectionDelayMax', 'randomizationFactor', 'timeout', 'autoConnect', 'parser', 'host', 'hostname', 'secure', 'port', 'query', 'agent', 'upgrade', 'forceBase64', 'timestampParam', 'timestampRequests', 'transports', 'rememberUpgrade', 'onlyBinaryUpgrades', 'requestTimeout', 'transportOptions', 'pfx', 'key', 'passphrase', 'cert', 'ca', 'ciphers', 'rejectUnauthorized', 'extraHeaders', 'withCredentials', 'closeOnBeforeunload', 'useNativeTimers', 'autoUnref', 'perMessageDeflate', 'addTrailingSlash', 'protocols', 'auth', 'retries', 'ackTimeout'.
Those elements have the following types:
  - `forceNew` (Bool; optional): Should we force a new Manager for this connection?
@,default,false
  - `multiplex` (Bool; optional): Should we multiplex our connection (reuse existing Manager) ?
@,default,true
  - `path` (String; optional): The path to get our client file from, in the case of the server
serving it
@,default,'/socket.io'
  - `reconnection` (Bool; optional): Should we allow reconnections?
@,default,true
  - `reconnectionAttempts` (Real; optional): How many reconnection attempts should we try?
@,default,Infinity
  - `reconnectionDelay` (Real; optional): The time delay in milliseconds between reconnection attempts
@,default,1000
  - `reconnectionDelayMax` (Real; optional): The max time delay in milliseconds between reconnection attempts
@,default,5000
  - `randomizationFactor` (Real; optional): Used in the exponential backoff jitter when reconnecting
@,default,0.5
  - `timeout` (Real; optional): The timeout in milliseconds for our connection attempt
@,default,20000
  - `autoConnect` (Bool; optional): Should we automatically connect?
@,default,true
  - `parser` (Bool | Real | String | Dict | Array; optional): the parser to use. Defaults to an instance of the Parser that ships with socket.io.
  - `host` (String; optional): The host that we're connecting to. Set from the URI passed when connecting
  - `hostname` (String; optional): The hostname for our connection. Set from the URI passed when connecting
  - `secure` (Bool; optional): If this is a secure connection. Set from the URI passed when connecting
  - `port` (String | Real; optional): The port for our connection. Set from the URI passed when connecting
  - `query` (Dict with Strings as keys and values of type Bool | Real | String | Dict | Array; optional): Any query parameters in our uri. Set from the URI passed when connecting
  - `agent` (String; optional): `http.Agent` to use, defaults to `false` (NodeJS only)

Note: the type should be "undefined | http.Agent | https.Agent | false", but this would break browser-only clients.
@,see,https,://nodejs.org/api/http.html#httprequestoptions-callback
  - `upgrade` (Bool; optional): Whether the client should try to upgrade the transport from
long-polling to something better.
@,default,true
  - `forceBase64` (Bool; optional): Forces base 64 encoding for polling transport even when XHR2
responseType is available and WebSocket even if the used standard
supports binary.
  - `timestampParam` (String; optional): The param name to use as our timestamp key
@,default,'t'
  - `timestampRequests` (Bool; optional): Whether to add the timestamp with each transport request. Note: this
is ignored if the browser is IE or Android, in which case requests
are always stamped
@,default,false
  - `transports` (Array of Strings; optional): A list of transports to try (in order). Engine.io always attempts to
connect directly with the first one, provided the feature detection test
for it passes.
@,default,['polling','websocket', 'webtransport']
  - `rememberUpgrade` (Bool; optional): If true and if the previous websocket connection to the server succeeded,
the connection attempt will bypass the normal upgrade process and will
initially try websocket. A connection attempt following a transport error
will use the normal upgrade process. It is recommended you turn this on
only when using SSL/TLS connections, or if you know that your network does
not block websockets.
@,default,false
  - `onlyBinaryUpgrades` (Bool; optional): Are we only interested in transports that support binary?
  - `requestTimeout` (Real; optional): Timeout for xhr-polling requests in milliseconds (0) (only for polling transport)
  - `transportOptions` (optional): Transport options for Node.js client (headers etc). transportOptions has the following type: lists containing elements 'constructor', 'toString', 'toLocaleString', 'valueOf', 'hasOwnProperty', 'isPrototypeOf', 'propertyIsEnumerable'.
Those elements have the following types:
  - `constructor` (optional): The initial value of Object.prototype.constructor is the standard built-in Object constructor.
  - `toString` (optional): Returns a string representation of an object.
  - `toLocaleString` (optional): Returns a date converted to a string using the current locale.
  - `valueOf` (optional): Returns the primitive value of the specified object.
  - `hasOwnProperty` (optional): Determines whether an object has a property with the specified name.
@,param,v, ,A property name.
  - `isPrototypeOf` (optional): Determines whether an object exists in another object's prototype chain.
@,param,v, ,Another object whose prototype chain is to be checked.
  - `propertyIsEnumerable` (optional): Determines whether a specified property is enumerable.
@,param,v, ,A property name.
  - `pfx` (String; optional): (SSL) Certificate, Private key and CA certificates to use for SSL.
Can be used in Node.js client environment to manually specify
certificate information.
  - `key` (String; optional): (SSL) Private key to use for SSL. Can be used in Node.js client
environment to manually specify certificate information.
  - `passphrase` (String; optional): (SSL) A string or passphrase for the private key or pfx. Can be
used in Node.js client environment to manually specify certificate
information.
  - `cert` (String; optional): (SSL) Public x509 certificate to use. Can be used in Node.js client
environment to manually specify certificate information.
  - `ca` (String | Array of Strings; optional): (SSL) An authority certificate or array of authority certificates to
check the remote host against.. Can be used in Node.js client
environment to manually specify certificate information.
  - `ciphers` (String; optional): (SSL) A string describing the ciphers to use or exclude. Consult the
[cipher format list]
(http://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT) for
details on the format.. Can be used in Node.js client environment to
manually specify certificate information.
  - `rejectUnauthorized` (Bool; optional): (SSL) If true, the server certificate is verified against the list of
supplied CAs. An 'error' event is emitted if verification fails.
Verification happens at the connection level, before the HTTP request
is sent. Can be used in Node.js client environment to manually specify
certificate information.
  - `extraHeaders` (Dict with Strings as keys and values of type String; optional): Headers that will be passed for each request to the server (via xhr-polling and via websockets).
These values then can be used during handshake or for special proxies.
  - `withCredentials` (Bool; optional): Whether to include credentials (cookies, authorization headers, TLS
client certificates, etc.) with cross-origin XHR polling requests
@,default,false
  - `closeOnBeforeunload` (Bool; optional): Whether to automatically close the connection whenever the beforeunload event is received.
@,default,false
  - `useNativeTimers` (Bool; optional): Whether to always use the native timeouts. This allows the client to
reconnect when the native timeout functions are overridden, such as when
mock clocks are installed.
@,default,false
  - `autoUnref` (Bool; optional): weather we should unref the reconnect timer when it is
create automatically
@,default,false
  - `perMessageDeflate` (optional): parameters of the WebSocket permessage-deflate extension (see ws module api docs). Set to false to disable.
@,default,false. perMessageDeflate has the following type: lists containing elements 'threshold'.
Those elements have the following types:
  - `threshold` (Real; required)
  - `addTrailingSlash` (Bool; optional): Whether we should add a trailing slash to the request path.
@,default,true
  - `protocols` (String | Array of Strings; optional): Either a single protocol string or an array of protocol strings. These strings are used to indicate sub-protocols,
so that a single server can implement multiple WebSocket sub-protocols (for example, you might want one server to
be able to handle different types of interactions depending on the specified protocol)
@,default,[]
  - `auth` (Dict with Strings as keys and values of type Bool | Real | String | Dict | Array; optional): the authentication payload sent when connecting to the Namespace
  - `retries` (Real; optional): The maximum number of retries. Above the limit, the packet will be discarded.

Using `Infinity` means the delivery guarantee is "at-least-once" (instead of "at-most-once" by default), but a
smaller value like 10 should be sufficient in practice.
  - `ackTimeout` (Real; optional): The default timeout in milliseconds used when waiting for an acknowledgement.
- `timeout` (Real; optional): Timeout in milliseconds for emitted events (0 means no timeout)
- `url` (String; optional): The socket.io server URL, defaults to window.location.origin
"""
function dashsocketio(; kwargs...)
        available_props = Symbol[:id, :autoConnect, :connected, :eventNames, :hasError, :lastError, :path, :reconnection, :reconnectionAttempts, :reconnectionDelay, :reconnectionDelayMax, :socketId, :socketOptions, :timeout, :url]
        wild_props = Symbol[]
        return Component("dashsocketio", "DashSocketIO", "dash_socketio", available_props, wild_props; kwargs...)
end

