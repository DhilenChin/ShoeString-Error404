# -*- coding: UTF-8 -*-

from fbchat import log, Client
from fbchat.models import *

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, process message
        if author_id != self.uid:
            global message
            global threadId
            global threadType
            message = message_object.text
            threadId = thread_id
            threadType = thread_type
        self.stopListening()
                




def recieveMessage():
    client.listen()
    print(message)
    return message

def sendMessage(message):
    client.send(Message(text=message), thread_id=threadId, thread_type=threadType)

client = EchoBot("boxwithabutton@gmail.com", "FUCKBotpress")
message = ""
threadId = ""
threadType = ""
print(recieveMessage())
sendMessage("Hi!")