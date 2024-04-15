# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashSocketIO <- function(id=NULL, debug=NULL, send=NULL, url=NULL) {
    
    props <- list(id=id, debug=debug, send=send, url=url)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSocketIO',
        namespace = 'dash_socketio',
        propNames = c('id', 'debug', 'send', 'url'),
        package = 'dashSocketio'
        )

    structure(component, class = c('dash_component', 'list'))
}
