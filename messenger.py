"""
Created on Tue Nov  5 15:19:31 2024

@author: ngs
"""
from argparse import ArgumentParser

from remote_server import RemoteServer
from client import Client
from local_server import Server

argument_parser = ArgumentParser()
argument_parser.add_argument('-f', '--filename', help='Chemin du fichier JSON dans lequel les données du serveur sont stockées')
argument_parser.add_argument('-u','--url')
arguments = argument_parser.parse_args()
# Vous devez préciser que `server` peut être un objet
# de type `Server` ou `RemoteServer`.
server : Server | RemoteServer
if arguments.filename is not None :
    server = Server.load_from_json_file(arguments.filename)
elif arguments.url is not None :
    server = RemoteServer(arguments.url)
else :
    print('Error, -j or -u should be set')
    exit(-1)

client = Client(server)
client.accueil()
# print(server.get_users())


