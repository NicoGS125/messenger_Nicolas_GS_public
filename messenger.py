from datetime import datetime

"""
Created on Tue Nov  5 15:19:31 2024

@author: ngs
"""
import json
from datetime import datetime

def load_server() :
    with open('server_json.json') as json_file:
        server = json.load(json_file)
        server.users = [User.conversion_dico_User(elem) for elem in server['users']]
        server.channels = [Channels.conversion_dico_Channels(channels) for channels in server['channels']]
        server.message = [Message.conversion_dico_Message(message) for message in server['message']]
    return server

server = load_server()

def accueil() :
    print('=== Messenger ===')
    print('x. Leave')
    print('1.See users')
    print('2.See channels')
    print('3.See messages')
    choice = input('Select an option: ')
    if choice == 'x':
        print('Bye!')
    elif choice == '1':
        for elem in server.users :
            print(elem.id,",",elem.name)
    elif choice == '2':
        for elem in server.channels:
            print(elem.name)
    elif choice == '3':
        choice2 = input("de quel groupe voulez vous voir le message (entrer l'id)")
        L = []
        M = [m for m in server.message if m.channel == int(choice2)]
        print(M)
        for elem in M:
            L.append(elem.content)
        print(L)
    else:
        print('Unknown option:', choice)

def id_to_name(id):
    liste = []
    for dico in server.users:
        l = [key for key in dico.keys()]
        if dico[l[0]]==id:
            liste.append(dico[l[1]])
    return liste[0]

def id_to_name2(id):
    L = []
    for elem in server['users']:
        if elem.id == id :
            L.append(elem.name)
    return L[0]

print(id_to_name(1))

def nv_groupe(name, member_ids):
    new_channel_id = max(channel.id for channel in server['channels']) + 1
    new_channel = {"id": new_channel_id, "name": name, "member_id": member_ids}
    server.channels.append(Channels.conversion_dico_Channels(new_channel))
    print(f"\nNouveau canal ajouté : {new_channel}")
    return new_channel

def new_user(prénom):
    nom = input
    n_id = max(user.id for user in server['users'])+1
    server.users.append(User.conversion_dico_User({'id': n_id,'name':nom}))

def sauvegarde_fichier():
    with open('server_json.json', 'w') as file :
         json.dump()

class User:
    def __init__(self, id: int, name : str):
        self.id = id
        self.name = name
    @classmethod
    def conversion_dico_User(cls, user : 'dict') -> 'User':
        return cls(user['id'],user['Name'])
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


    









    




