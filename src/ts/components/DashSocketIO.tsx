import React, { useState } from 'react';
import { io } from 'socket.io-client';
import { DashComponentProps } from '../props';

type Props = {
  url: string,
  debug?: boolean,
  send?: object,
} & DashComponentProps;

const DashSocketIO = (props: Props) => {
  const { url, send, debug = false, setProps } = props;

  const [socketId, setSocketId] = useState<string | null>(null);
  const [connected, setConnected] = useState<boolean>(false);

  const socket = React.useMemo(() => io(
    url || undefined, { auth: { pathname: window.location.pathname } }
  ), [url])

  React.useEffect(() => {
    const onConnect = () => {
      if (debug) {
        console.log(`Connected at ${new Date().toISOString()}`)
      }
      setSocketId(socket.id);
      setConnected(true);
    }

    const onDisconnect = () => {
      if (debug) {
        console.log(`Disconnected at ${new Date().toISOString()}`)
      }
      setSocketId(null);
      setConnected(false);
    }

    const onEvent = (event: object) => {
      if (debug) {
        console.log(`Event received at ${new Date().toISOString()} - ${JSON.stringify(event)}`)
      }
      for (const [key, value] of Object.entries(event)) {
        var data_key = `data-${key}`
        if (debug) {
          console.log(`Setting ${data_key} to ${value}`)
        }
        // Jim: In case the suuplied value equals the current value, we need to set it to null first
        // otherwise react won't update the value in the frontend as there is no change.
        // I don't think this incurs a performance penalty but please correct me if I'm wrong.
        setProps({ [data_key]: null })
        setProps({ [data_key]: value })
      }
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on("ws-event", onEvent);

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
      socket.off("ws-event", onEvent);
      socket.disconnect();
    };
  }, [socket]);

  React.useEffect(() => {
    if (socket && send) {
      const event = send['event'];
      const data = send['data'];

      if (data) {
        if (debug) {
          console.log(`Sending event ${event} at ${new Date().toISOString()} - ${JSON.stringify(data)}`)
        }
        socket.emit(event, data);
      } else {
        if (debug) {
          console.log(`Sending event ${event} at ${new Date().toISOString()}`)
        }
        socket.emit(event);
      }
    }
  }, [send]);

  return null;
}

DashSocketIO.defaultProps = {};

export default DashSocketIO;
