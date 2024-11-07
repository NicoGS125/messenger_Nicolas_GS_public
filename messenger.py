from datetime import datetime

"""
Created on Tue Nov  5 15:19:31 2024

@author: ngs
"""
import json
from datetime import datetime

with open('server_json.json') as file:
  server = json.load(file)

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
        for elem in server['users'] :
            print(elem['id'],",",elem['name'])
    elif choice == '2':
        L = []
        liste = [c for c in server['channels'][0].keys()]
        for elem in liste :
            L.append(server['channels'][0][elem])
        print(L)
    elif choice == '3':
        choice2 = input("de quel groupe voulez vous voir le message (entrer l'id)")
        L = []
        M = [m for m in server['messages'] if m['channel'] == int(choice2)]
        print(M)
        for elem in M:
            L.append(elem['content'])
        print(L)
    else:
        print('Unknown option:', choice)

def id_to_name(id):
    liste = []
    for dico in server['users']:
        l = [c for c in dico.keys()]
        if dico[l[0]]==id:
            liste.append(dico[l[1]])
    return liste[0]

def id_to_name2(id):
    L = []
    for elem in server['users']:
        if elem['id'] == id :
            L.append(elem['name'])
    return L[0]

print(id_to_name(1))

def nv_groupe(name, member_ids):
    new_channel_id = len(server['channels']) + 1
    new_channel = {"id": new_channel_id, "name": name, "member_id": member_ids}
    server['channels'].append(new_channel)
    print(f"\nNouveau canal ajouté : {new_channel}")
    return new_channel

def new_user(prénom):
    nom = input
    n_id = max(dico['id'] for dico in server['users'])+1
    server['users'].append({'id': n_id,'name':nom})


def sauvegarde_fichier():
    with open('server_json.json', 'w') as file :
         json.dump()

    




