import React from 'react';
import { io } from 'socket.io-client';
import {DashComponentProps} from '../props';

type Props = {
  /** The socket.io server URL */
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
    ), [])

    React.useEffect(() => {
      function onConnect() {
        setProps({connected: true, socketId: socket.id});
      }

      function onDisconnect() {
        setProps({connected: false, socketId: null});
      }

      socket.on('connect', onConnect);
      socket.on('disconnect', onDisconnect);

      return () => {
        socket.off('connect', onConnect);
        socket.off('disconnect', onDisconnect);
        socket.disconnect();
      };
    }, []);

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
    }, [eventNames])

    return null
}

DashSocketIO.defaultProps = {};

export default DashSocketIO;
