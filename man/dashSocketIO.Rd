% Auto-generated: do not edit by hand
\name{socketIO}

\alias{socketIO}

\title{DashSocketIO component}

\description{
Socket.IO Dash component.
}

\usage{
socketIO(id=NULL, connected=NULL, eventNames=NULL, url=NULL)
}

\arguments{
\item{id}{Character. Unique ID to identify this component in Dash callbacks.}

\item{connected}{Logical. Whether the client is connected to the websocket - READONLY}

\item{eventNames}{List of characters. Name of Socket.IO events to listen to}

\item{url}{Character. The socket.io server URL}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

