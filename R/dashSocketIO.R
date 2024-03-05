# AUTO GENERATED FILE - DO NOT EDIT

#' @export
socketIO <- function(id=NULL, connected=NULL, eventNames=NULL, url=NULL) {

    props <- list(id=id, connected=connected, eventNames=eventNames, url=url)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSocketIO',
        namespace = 'dash_socketio',
        propNames = c('id', 'connected', 'eventNames', 'url'),
        package = 'dashSocketio'
        )

    structure(component, class = c('dash_component', 'list'))
}
