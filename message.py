class Message :
    def __init__(self, id : int, reception_date = str, sender_id = int, channel = int, content =str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content
    @classmethod
    def conversion_dico_Message(cls, message : 'dict') -> 'Message':
            return cls(message['id'], message['reception_date'], message['sender_id'], message['channel'], message['content'])
    def conversion_Message_dico(self) -> 'dict':
            return {'id':self.id, 'reception_date':self.reception_date, 'sender_id': self.sender_id, 'channel':self.channel, 'content':self.content}