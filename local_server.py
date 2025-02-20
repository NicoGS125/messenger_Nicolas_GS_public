import json
from channel import Channels
from user import User
from message import Message

class Server : 
    def __init__(self, users : list[User], channels : list[Channels], message : list[Message]):
        self.users = users
        self.channels = channels
        self.message = message

    def get_users(self) -> 'list[User]':
        return self.users

    @classmethod
    def load_from_json_file(cls, json_file_path: str) -> 'Server':
        with open(json_file_path) as json_file:
            server_as_class = cls([],[],[])
            server = json.load(json_file)
            server_as_class.users = [User.conversion_dico_User(elem) for elem in server["users"]]
            server_as_class.channels = [Channels.conversion_dico_Channels(channels) for channels in server['channels']]
            server_as_class.message = [Message.conversion_dico_Message(message) for message in server['message']]
        return server_as_class
    
    def save_to_json_file(self, json_file_path: str):
        server_as_dict = {
            'users': [],
            'channels': [],
            'message': [],
        }
        for user in self.users:
            server_as_dict['users'].append(User.conversion_User_dico(user))
        for channel in self.channels:
            server_as_dict['channels'].append(Channels.conversion_Channels_dico(channel))
        for message in self.message:
            server_as_dict['message'].append(Message.conversion_Message_dico(message))
        with open(json_file_path, 'w') as json_file :
            json.dump(server_as_dict, json_file)

    def id_to_channel(self,numero):
        for elem in self.server.channels:
            if numero == elem.id :
                return elem
    
    def id_to_name2(self, id):
        L = []
        for elem in self.users:
            L.append(elem.name)
        return L[0]