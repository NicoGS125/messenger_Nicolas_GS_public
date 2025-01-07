"""
Created on Tue Nov  5 15:19:31 2024

@author: ngs
"""
from argparse import ArgumentParser
import json

class User:
    def __init__(self, id: int, name : str):
        self.id = id
        self.name = name
    @classmethod
    def conversion_dico_User(cls, user : 'dict') -> 'User':
        return cls(user['id'],user['name'])
    def conversion_User_dico(self):
        return{'id':self.id, 'name': self.name}

class Channels :
    def __init__(self, id: int, name: str, member_id : list):
        self.id = id
        self.name = name
        self.member_id = member_id
    @classmethod
    def conversion_dico_Channels(cls, channels : 'dict') -> 'Channels':
        return cls(channels['id'], channels['name'], channels['member_id'])
    def conversion_Channels_dico(self):
        return{'id': self.id, 'name': self.name, 'member_id': self.member_id}

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


class Server : 
    def __init__(self, users : list[User], channels : list[Channels], message : list[Message]):
        self.users = users
        self.channels = channels
        self.message = message

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

    def id_to_name2(self, id):
        L = []
        for elem in self.users:
            L.append(elem.name)
        return L[0]

class Client :
    def __init__(self, server : Server):
        self.server = server

    def nv_channel(self, name, member_ids):
        new_channel_id = max(channel.id for channel in self.server.channels) + 1
        new_channel = {"id": new_channel_id, "name": name, "member_id": member_ids}
        self.server.channels.append(Channels.conversion_dico_Channels(new_channel))
        print(f"\nNouveau canal ajouté : {new_channel}")
        return new_channel

    def new_user(self):
        nom = input("choisissez un prénom")
        n_id = max(user.id for user in self.server['users'])+1
        self.server.users.append(User.conversion_dico_User({'id': n_id,'name':nom}))

    def accueil(self) :
        print('=== Messenger ===')
        print('x. Leave')
        print('1.See users')
        print('2.See channels')
        print('3.See messages')
        choice = input('Select an option: ')
        if choice == 'x':
            print('Bye!')
        elif choice == '1':
            for elem in self.server.users :
                print(elem.id,",",elem.name)
        elif choice == '2':
            for elem in self.server.channels:
                print(elem.name)
        elif choice == '3':
            choice2 = input("de quel groupe voulez vous voir le message (entrer l'id)")
            L = []
            M = [m for m in self.server.message if m.channel == int(choice2)]
            print(M)
            for elem in M:
                L.append(elem.content)
            print(L)
        else:
            print('Unknown option:', choice)

argument_parser = ArgumentParser()
argument_parser.add_argument('-j', '--jsonfile', default='server_json.json', help='Chemin du fichier JSON dans lequel les données du serveur sont stockées')
arguments = argument_parser.parse_args()

server = Server.load_from_json_file(arguments.jsonfile)
client = Client(server)
client.accueil()
