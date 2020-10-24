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
            incoming = message_object.text
            replies = generateReplies(incoming)
            for reply in replies:
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)


def generateReplies(incoming):
    reversed = ""
    for i in range(1, len(incoming)+1):
        reversed += incoming[len(incoming)-i]
        
    return ["Recieved the following message: \"{}\"".format(incoming), incoming, reversed, incoming, "Ok, by now!"]


client = EchoBot("boxwithabutton@gmail.com", "FUCKBotpress")
client.listen()