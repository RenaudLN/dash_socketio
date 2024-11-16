import React from 'react';
import { io, Socket, ManagerOptions, SocketOptions } from 'socket.io-client';
import { DashComponentProps } from '../props';

type Props = {
  /** The socket.io server URL, defaults to window.location.origin */
  url?: string;
  /** The path for the Socket.IO endpoint, defaults to '/socket.io' */
  path?: string;
  /** Name of Socket.IO events to listen to */
  eventNames?: string[];
  /** Whether the client is connected to the websocket - READONLY */
  connected?: boolean;
  /** The socket ID - READONLY */
  socketId?: string;
  /** Whether to automatically connect on component mount */
  autoConnect?: boolean;
  /** Timeout in milliseconds for emitted events (0 means no timeout) */
  timeout?: number;
  /** Number of reconnection attempts before giving up */
  reconnectionAttempts?: number;
  /** Initial delay in milliseconds before reconnection attempt */
  reconnectionDelay?: number;
  /** Maximum delay in milliseconds between reconnection attempts */
  reconnectionDelayMax?: number;
  /** Whether to enable reconnection */
  reconnection?: boolean;
  /** Additional Socket.IO options */
  socketOptions?: Partial<ManagerOptions & SocketOptions>;
  /** Last error encountered - READONLY */
  lastError?: Error | null;
  /** Whether socket has failed to connect - READONLY */
  hasError?: boolean;
} & DashComponentProps;

const DashSocketIO = (props: Props) => {
    const {
        url,
        path,
        setProps,
        eventNames,
        autoConnect = true,
        timeout = 5000,
        reconnectionAttempts = Infinity,
        reconnectionDelay = 1000,
        reconnectionDelayMax = 5000,
        reconnection = true,
        socketOptions = {},
    } = props;

    const [socket, setSocket] = React.useState<Socket | null>(null);
    const componentRef = React.useRef<any>(null);

    // Create socket instance
    React.useEffect(() => {
        const newSocket = io(url || undefined, {
            path: path || '/socket.io',
            auth: { pathname: window.location.pathname },
            autoConnect,
            timeout,
            reconnectionAttempts,
            reconnectionDelay,
            reconnectionDelayMax,
            reconnection,
            ...socketOptions
        });

        setSocket(newSocket);

        return () => {
            if (newSocket) {
                newSocket.disconnect();
            }
        };
    }, [url, path, autoConnect, timeout, reconnectionAttempts, 
        reconnectionDelay, reconnectionDelayMax, reconnection]);

    // Handle connection events
    React.useEffect(() => {
        if (!socket) return;

        const handleConnect = () => {
            setProps({
                connected: true,
                socketId: socket.id,
                hasError: false,
                lastError: null
            });
        };

        const handleConnectError = (error: Error) => {
            setProps({
                connected: false,
                socketId: null,
                hasError: true,
                lastError: error
            });
        };

        const handleDisconnect = () => {
            setProps({
                connected: false,
                socketId: null
            });
        };

        socket.on('connect', handleConnect);
        socket.on('connect_error', handleConnectError);
        socket.on('disconnect', handleDisconnect);

        return () => {
            socket.off('connect', handleConnect);
            socket.off('connect_error', handleConnectError);
            socket.off('disconnect', handleDisconnect);
        };
    }, [socket, setProps]);

    // Handle custom events
    React.useEffect(() => {
        if (!socket || !eventNames?.length) return;

        const eventHandlers = new Map<string, (data: any) => void>();

        eventNames.forEach(eventName => {
            const handler = (data: any) => {
                setProps({ [`data-${eventName}`]: data });
            };
            eventHandlers.set(eventName, handler);
            socket.on(eventName, handler);
        });

        return () => {
            eventHandlers.forEach((handler, eventName) => {
                socket.off(eventName, handler);
            });
        };
    }, [socket, eventNames, setProps]);

    // Expose methods through useImperativeHandle
    React.useImperativeHandle(
        componentRef,
        () => ({
            connect: () => socket?.connect(),
            disconnect: () => socket?.disconnect(),
            emit: (eventName: string, ...args: any[]) => socket?.emit(eventName, ...args),
            getSocket: () => socket,
        }),
        [socket]
    );

    return null;
};

DashSocketIO.defaultProps = {
    path: '/socket.io',
    autoConnect: true,
    timeout: 5000,
    reconnectionAttempts: Infinity,
    reconnectionDelay: 1000,
    reconnectionDelayMax: 5000,
    reconnection: true,
    socketOptions: {},
    connected: false,
    hasError: false,
    lastError: null
};

export default DashSocketIO;