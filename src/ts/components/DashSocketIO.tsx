import React from 'react';
import { io } from 'socket.io-client';
import { DashComponentProps } from '../props';

type SocketOptions = {
  /** The socket.io endpoint path, defaults to '/socket.io' */
  path?: string;
  /** Whether to force a new connection */
  forceNew?: boolean;
  /** Timeout in milliseconds */
  timeout?: number;
  /** Whether to automatically connect on creation */
  autoConnect?: boolean;
  /** Additional query parameters */
  query?: Record<string, any>;
  /** Authentication data */
  auth?: Record<string, any>;
  [key: string]: any;
};

type Props = {
  /** The socket.io namespace url, defaults to window.location.origin */
  url?: string;
  /** Socket.IO connection options */
  options?: Partial<SocketOptions>;
  /** Name of Socket.IO events to listen to */
  eventNames?: string[];
  /** Whether the client is connected to the websocket - READONLY */
  connected?: boolean;
  /** The socket ID */
  socketId?: string;
} & DashComponentProps;

const defaultOptions: SocketOptions = {
  path: '/socket.io',
  forceNew: false,
  autoConnect: true
};

/**
 * Socket.IO Dash component.
 */
const DashSocketIO = (props: Props) => {
  const { url, options = {}, setProps, eventNames } = props;

  const socket = React.useMemo(() => io(
    url || undefined,
    {
      ...defaultOptions,
      ...options,
      auth: {
        ...options.auth,
        pathname: window.location.pathname
      }
    }
  ), [url, options]);

  React.useEffect(() => {
    const onConnect = () => {
      setProps({ connected: true, socketId: socket.id });
    }

    const onDisconnect = () => {
      setProps({ connected: false, socketId: null });
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
      socket.disconnect();
    };
  }, [socket]);

  React.useEffect(() => {
    if (!eventNames || eventNames.length === 0) {
      return;
    }
    function onEvent(eventName: string) {
      return (data: any) => {
        setProps({ [`data-${eventName}`]: data });
      }
    }
    eventNames.forEach((eventName) => socket.on(eventName, onEvent(eventName)));
    return () => {
      eventNames.forEach((eventName) => socket.off(eventName, onEvent(eventName)));
    };
  }, [socket, eventNames])

  return null;
}

export default DashSocketIO;