# routing.py
from channels.routing import route
from chat.consumers import *

channel_routing = [
    route('websocket.receive', ws_echo),
]