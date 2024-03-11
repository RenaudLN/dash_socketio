import React from 'react';
import { io } from 'socket.io-client';
import {DashComponentProps} from '../props';

type Props = {
  /** The socket.io namespace url, defaults to window.location.origin */
  url?: string
  /** Name of Socket.IO events to listen to */
  eventNames?: string[]
  /** Whether the client is connected to the websocket - READONLY */
  connected?: boolean
  /** The socket ID */
  socketId?: string
} & DashComponentProps;
/**
 * Socket.IO Dash component.
 */
const DashSocketIO = (props: Props) => {
    const { url, setProps, eventNames } = props;

    const socket = React.useMemo(() => io(
      url || undefined, {auth: {pathname: window.location.pathname}}
    ), [url])

    React.useEffect(() => {
      const onConnect = () => {
        setProps({connected: true, socketId: socket.id});
      }

      const onDisconnect = () => {
        setProps({connected: false, socketId: null});
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
          setProps({[`data-${eventName}`]: data});
        }
      }
      eventNames.forEach((eventName) => socket.on(eventName, onEvent(eventName)));
      return () => {
        eventNames.forEach((eventName) => socket.off(eventName, onEvent(eventName)));
      };
    }, [socket, eventNames])

    return null
}

DashSocketIO.defaultProps = {};

export default DashSocketIO;
