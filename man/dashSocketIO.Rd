% Auto-generated: do not edit by hand
\name{dashSocketIO}

\alias{dashSocketIO}

\title{DashSocketIO component}

\description{

}

\usage{
dashSocketIO(id=NULL, autoConnect=NULL, connected=NULL, eventNames=NULL,
hasError=NULL, lastError=NULL, path=NULL, reconnection=NULL,
reconnectionAttempts=NULL, reconnectionDelay=NULL,
reconnectionDelayMax=NULL, socketId=NULL,
socketOptions=NULL, timeout=NULL, url=NULL)
}

\arguments{
\item{id}{Character. Unique ID to identify this component in Dash callbacks.}

\item{autoConnect}{Logical. Whether to automatically connect on component mount}

\item{connected}{Logical. Whether the client is connected to the websocket - READONLY}

\item{eventNames}{List of characters. Name of Socket.IO events to listen to}

\item{hasError}{Logical. Whether socket has failed to connect - READONLY}

\item{lastError}{Lists containing elements 'name', 'message', 'stack'.
those elements have the following types:
  - name (character; required)
  - message (character; required)
  - stack (character; optional). Last error encountered - READONLY}

\item{path}{Character. The path for the Socket.IO endpoint, defaults to '/socket.io'}

\item{reconnection}{Logical. Whether to enable reconnection}

\item{reconnectionAttempts}{Numeric. Number of reconnection attempts before giving up}

\item{reconnectionDelay}{Numeric. Initial delay in milliseconds before reconnection attempt}

\item{reconnectionDelayMax}{Numeric. Maximum delay in milliseconds between reconnection attempts}

\item{socketId}{Character. The socket ID - READONLY}

\item{socketOptions}{Lists containing elements 'forcenew', 'multiplex', 'path', 'reconnection', 'reconnectionattempts', 'reconnectiondelay', 'reconnectiondelaymax', 'randomizationfactor', 'timeout', 'autoconnect', 'parser', 'host', 'hostname', 'secure', 'port', 'query', 'agent', 'upgrade', 'forcebase64', 'timestampparam', 'timestamprequests', 'transports', 'rememberupgrade', 'onlybinaryupgrades', 'requesttimeout', 'transportoptions', 'pfx', 'key', 'passphrase', 'cert', 'ca', 'ciphers', 'rejectunauthorized', 'extraheaders', 'withcredentials', 'closeonbeforeunload', 'usenativetimers', 'autounref', 'permessagedeflate', 'addtrailingslash', 'protocols', 'auth', 'retries', 'acktimeout'.
those elements have the following types:
  - forcenew (logical; optional): should we force a new manager for this connection?
@,default,false
  - multiplex (logical; optional): should we multiplex our connection (reuse existing manager) ?
@,default,true
  - path (character; optional): the path to get our client file from, in the case of the server
serving it
@,default,'/socket.io'
  - reconnection (logical; optional): should we allow reconnections?
@,default,true
  - reconnectionattempts (numeric; optional): how many reconnection attempts should we try?
@,default,infinity
  - reconnectiondelay (numeric; optional): the time delay in milliseconds between reconnection attempts
@,default,1000
  - reconnectiondelaymax (numeric; optional): the max time delay in milliseconds between reconnection attempts
@,default,5000
  - randomizationfactor (numeric; optional): used in the exponential backoff jitter when reconnecting
@,default,0.5
  - timeout (numeric; optional): the timeout in milliseconds for our connection attempt
@,default,20000
  - autoconnect (logical; optional): should we automatically connect?
@,default,true
  - parser (logical | numeric | character | named list | unnamed list; optional): the parser to use. defaults to an instance of the parser that ships with socket.io.
  - host (character; optional): the host that we're connecting to. set from the uri passed when connecting
  - hostname (character; optional): the hostname for our connection. set from the uri passed when connecting
  - secure (logical; optional): if this is a secure connection. set from the uri passed when connecting
  - port (character | numeric; optional): the port for our connection. set from the uri passed when connecting
  - query (list with named elements and values of type logical | numeric | character | named list | unnamed list; optional): any query parameters in our uri. set from the uri passed when connecting
  - agent (character; optional): `http.agent` to use, defaults to `false` (nodejs only)

note: the type should be "undefined | http.agent | https.agent | false", but this would break browser-only clients.
@,see,https,://nodejs.org/api/http.html#httprequestoptions-callback
  - upgrade (logical; optional): whether the client should try to upgrade the transport from
long-polling to something better.
@,default,true
  - forcebase64 (logical; optional): forces base 64 encoding for polling transport even when xhr2
responsetype is available and websocket even if the used standard
supports binary.
  - timestampparam (character; optional): the param name to use as our timestamp key
@,default,'t'
  - timestamprequests (logical; optional): whether to add the timestamp with each transport request. note: this
is ignored if the browser is ie or android, in which case requests
are always stamped
@,default,false
  - transports (list of characters; optional): a list of transports to try (in order). engine.io always attempts to
connect directly with the first one, provided the feature detection test
for it passes.
@,default,['polling','websocket', 'webtransport']
  - rememberupgrade (logical; optional): if true and if the previous websocket connection to the server succeeded,
the connection attempt will bypass the normal upgrade process and will
initially try websocket. a connection attempt following a transport error
will use the normal upgrade process. it is recommended you turn this on
only when using ssl/tls connections, or if you know that your network does
not block websockets.
@,default,false
  - onlybinaryupgrades (logical; optional): are we only interested in transports that support binary?
  - requesttimeout (numeric; optional): timeout for xhr-polling requests in milliseconds (0) (only for polling transport)
  - transportoptions (optional): transport options for node.js client (headers etc). transportoptions has the following type: lists containing elements 'constructor', 'tostring', 'tolocalestring', 'valueof', 'hasownproperty', 'isprototypeof', 'propertyisenumerable'.
those elements have the following types:
  - constructor (optional): the initial value of object.prototype.constructor is the standard built-in object constructor.
  - tostring (optional): returns a string representation of an object.
  - tolocalestring (optional): returns a date converted to a string using the current locale.
  - valueof (optional): returns the primitive value of the specified object.
  - hasownproperty (optional): determines whether an object has a property with the specified name.
@,param,v, ,a property name.
  - isprototypeof (optional): determines whether an object exists in another object's prototype chain.
@,param,v, ,another object whose prototype chain is to be checked.
  - propertyisenumerable (optional): determines whether a specified property is enumerable.
@,param,v, ,a property name.
  - pfx (character; optional): (ssl) certificate, private key and ca certificates to use for ssl.
can be used in node.js client environment to manually specify
certificate information.
  - key (character; optional): (ssl) private key to use for ssl. can be used in node.js client
environment to manually specify certificate information.
  - passphrase (character; optional): (ssl) a string or passphrase for the private key or pfx. can be
used in node.js client environment to manually specify certificate
information.
  - cert (character; optional): (ssl) public x509 certificate to use. can be used in node.js client
environment to manually specify certificate information.
  - ca (character | list of characters; optional): (ssl) an authority certificate or array of authority certificates to
check the remote host against.. can be used in node.js client
environment to manually specify certificate information.
  - ciphers (character; optional): (ssl) a string describing the ciphers to use or exclude. consult the
[cipher format list]
(http://www.openssl.org/docs/apps/ciphers.html#cipher_list_format) for
details on the format.. can be used in node.js client environment to
manually specify certificate information.
  - rejectunauthorized (logical; optional): (ssl) if true, the server certificate is verified against the list of
supplied cas. an 'error' event is emitted if verification fails.
verification happens at the connection level, before the http request
is sent. can be used in node.js client environment to manually specify
certificate information.
  - extraheaders (list with named elements and values of type character; optional): headers that will be passed for each request to the server (via xhr-polling and via websockets).
these values then can be used during handshake or for special proxies.
  - withcredentials (logical; optional): whether to include credentials (cookies, authorization headers, tls
client certificates, etc.) with cross-origin xhr polling requests
@,default,false
  - closeonbeforeunload (logical; optional): whether to automatically close the connection whenever the beforeunload event is received.
@,default,false
  - usenativetimers (logical; optional): whether to always use the native timeouts. this allows the client to
reconnect when the native timeout functions are overridden, such as when
mock clocks are installed.
@,default,false
  - autounref (logical; optional): weather we should unref the reconnect timer when it is
create automatically
@,default,false
  - permessagedeflate (optional): parameters of the websocket permessage-deflate extension (see ws module api docs). set to false to disable.
@,default,false. permessagedeflate has the following type: lists containing elements 'threshold'.
those elements have the following types:
  - threshold (numeric; required)
  - addtrailingslash (logical; optional): whether we should add a trailing slash to the request path.
@,default,true
  - protocols (character | list of characters; optional): either a single protocol string or an array of protocol strings. these strings are used to indicate sub-protocols,
so that a single server can implement multiple websocket sub-protocols (for example, you might want one server to
be able to handle different types of interactions depending on the specified protocol)
@,default,[]
  - auth (list with named elements and values of type logical | numeric | character | named list | unnamed list; optional): the authentication payload sent when connecting to the namespace
  - retries (numeric; optional): the maximum number of retries. above the limit, the packet will be discarded.

using `infinity` means the delivery guarantee is "at-least-once" (instead of "at-most-once" by default), but a
smaller value like 10 should be sufficient in practice.
  - acktimeout (numeric; optional): the default timeout in milliseconds used when waiting for an acknowledgement.. Additional Socket.IO options}

\item{timeout}{Numeric. Timeout in milliseconds for emitted events (0 means no timeout)}

\item{url}{Character. The socket.io server URL, defaults to window.location.origin}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

