import requests
from user import User

class RemoteServer :
    def __init__(self, server_url):
        self.server_url = server_url

    def get_users(self) -> list[User]:
        # Il vaut mieux stocker la partie de base de l'URL
        # (https://groupe5-python-mines.fr) puis rajouter les morceaux
        # qui varient en fonction des requêtes (/users, /channels...)
        reponse = requests.get(f'{self.server_url}/users')
        users = reponse.json()
        list_User = []
        for elem in users :
            elem = User.conversion_dico_User(elem)
            list_User.append(elem)
        return list_User

    # Pas besoin de donner l'URL en paramètre, elle est déjà stockée dans `self`.
    # En revanche pour créer un utilisateur, il faut au moins lui donner un nom.
    def create_user(self, user_name: str) -> None:
        reponse = requests.post(f'{self.server_url}/users/create', json={'name': user_name})
        if 200 <= reponse.status_code < 300:
            print("Utilisateur ajouté avec succès!")
        else:
            print(f"Erreur lors de l'ajout de l'utilisateur: {reponse.status_code}")


