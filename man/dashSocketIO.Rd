% Auto-generated: do not edit by hand
\name{dashSocketIO}

\alias{dashSocketIO}

\title{DashSocketIO component}

\description{
Socket.IO Dash component.
}

\usage{
dashSocketIO(id=NULL, connected=NULL, eventNames=NULL, path=NULL,
socketId=NULL, url=NULL)
}

\arguments{
\item{id}{Character. Unique ID to identify this component in Dash callbacks.}

\item{connected}{Logical. Whether the client is connected to the websocket - READONLY}

\item{eventNames}{List of characters. Name of Socket.IO events to listen to}

\item{path}{Character. The socket.io endpoint path, defaults to '/socket.io'}

\item{socketId}{Character. The socket ID}

\item{url}{Character. The socket.io namespace url, defaults to window.location.origin}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

