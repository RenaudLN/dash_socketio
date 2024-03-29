# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashSocketIO <- function(id=NULL, connected=NULL, eventNames=NULL, socketId=NULL, url=NULL) {
    
    props <- list(id=id, connected=connected, eventNames=eventNames, socketId=socketId, url=url)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSocketIO',
        namespace = 'dash_socketio',
        propNames = c('id', 'connected', 'eventNames', 'socketId', 'url'),
        package = 'dashSocketio'
        )

    structure(component, class = c('dash_component', 'list'))
}
