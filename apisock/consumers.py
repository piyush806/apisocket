import re
import json
import logging
from channels import Group
from channels.sessions import channel_session


log = logging.getLogger(__name__)

# Create your views here.

@channel_session
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'accept':True,        
        })
    })

    pass

@channel_session
def ws_receive(message):
    pass

@channel_session
def ws_disconnect(message):
    pass
