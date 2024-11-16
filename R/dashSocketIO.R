# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashSocketIO <- function(id=NULL, autoConnect=NULL, connected=NULL, eventNames=NULL, hasError=NULL, lastError=NULL, path=NULL, reconnection=NULL, reconnectionAttempts=NULL, reconnectionDelay=NULL, reconnectionDelayMax=NULL, socketId=NULL, socketOptions=NULL, timeout=NULL, url=NULL) {
    
    props <- list(id=id, autoConnect=autoConnect, connected=connected, eventNames=eventNames, hasError=hasError, lastError=lastError, path=path, reconnection=reconnection, reconnectionAttempts=reconnectionAttempts, reconnectionDelay=reconnectionDelay, reconnectionDelayMax=reconnectionDelayMax, socketId=socketId, socketOptions=socketOptions, timeout=timeout, url=url)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSocketIO',
        namespace = 'dash_socketio',
        propNames = c('id', 'autoConnect', 'connected', 'eventNames', 'hasError', 'lastError', 'path', 'reconnection', 'reconnectionAttempts', 'reconnectionDelay', 'reconnectionDelayMax', 'socketId', 'socketOptions', 'timeout', 'url'),
        package = 'dashSocketio'
        )

    structure(component, class = c('dash_component', 'list'))
}
