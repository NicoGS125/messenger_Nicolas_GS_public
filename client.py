
from local_server import Server
from channel import Channels
from user import User


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

    def see_users(self):
        choix = input("de quel channel voulez vous voir les membres ?")
        if choix not in self.server.channels :
            return "il y a une erreur"
        liste_users_channel = []
        for elem in self.server.message :
            if elem.channel == choix and elem.sender_id not in liste_users_channel : 
                liste_users_channel.append(elem.sender_id)

    def see_channels(self):
        choix = input("quel channel voulez voir ?")
        if choix not in self.server.channels :
            return "il y a une erreur"
        liste_message = []
        for elem in self.server.message : 
            if elem.channel == choix :
                liste_message.append(elem)
        return liste_message
          
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