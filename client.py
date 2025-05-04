
from local_server import Server
from remote_server import RemoteServer
from channel import Channels
from user import User


class Client :
    def __init__(self, server : Server | RemoteServer):
        self.server = server

    def nv_channel(self, name, member_ids):
        # Idem que pour new_user
        new_channel_id = max(channel.id for channel in self.server.channels) + 1
        new_channel = {"id": new_channel_id, "name": name, "member_id": member_ids}
        # Pourquoi créer un dictionnaire et passer par la fonction
        # de conversion ? Vous pouvez créer un `Channels` directement
        # avec l'appel `Channel(new_channel_id, name, member_ids)`
        self.server.channels.append(Channels.conversion_dico_Channels(new_channel))
        print(f"\nNouveau canal ajouté : {new_channel}")
        return new_channel

    def new_user(self) -> None:
        nom = input("choisissez un prénom")
        # Cette logique doit être déléguée au `Server` et au `RemoteServer`.
        # Ces 2 lignes n'avaient pas de sens pour le `RemoteServer`
        self.server.create_user(nom)
        return self.accueil()

    def see_users(self):
        choix = input("de quel channel voulez vous voir les membres ?")
        if choix not in self.server.channels :
            # Soyez plus explicite dans vos messages d'erreur,
            # par exemple `f"Channel {choix} inconnu.`
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
          
    def accueil(self) -> None:
        print('=== Messenger ===')
        print('x. Leave')
        print('1.See users')
        print('2.See channels')
        print('3.See messages')
        choice = input('Select an option: ')
        if choice == 'x':
            print('Bye!')
        elif choice == '1':
            # Il vaut mieux utiliser un nom de variable qui représente
            # son contenu. Le mot `elem` fait uniquement référence
            # au contenant ("élément" fait référence à la liste)
            for user in self.server.get_users() :
                print(user.id,",",user.name)
        elif choice == '2':
            # Comme pour les users, il faudra créer une fonction
            # `get_channels` dans `Server` et dans `RemoteServer`
            for channel in self.server.channels:
                print(channel.name)
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