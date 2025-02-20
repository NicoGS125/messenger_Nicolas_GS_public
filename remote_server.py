import requests
from user import User

class RemoteServer :
    def __init__(self, server_url):
        self.server_url = server_url

    def get_users(self) -> list[User]:
        reponse = requests.get(self.server_url)
        users = reponse.json()
        list_User = []
        for elem in users :
            elem = User.conversion_dico_User(elem)
            list_User.append(elem)
        return list_User

    def create_users(self, server_url) :
        reponse = requests.post(server_url)
        if reponse.status_code == 201:
            print("Utilisateur ajouté avec succès!")
        else:
            print(f"Erreur lors de l'ajout de l'utilisateur: {reponse.status_code}")


