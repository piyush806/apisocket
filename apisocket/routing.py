from channels.staticfiles import StaticFilesConsumer
from apisock.consumers import *

channel_routing = {
    'websocket.connect': ws_connect,
    'websocket.receive': ws_receive,
    'websocket.disconnect': ws_disconnect,
}
