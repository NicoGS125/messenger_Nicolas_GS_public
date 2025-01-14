"""
Created on Tue Nov  5 15:19:31 2024

@author: ngs
"""
from argparse import ArgumentParser
import json
import requests

from remoteserver import RemoteServer
from client import Client
from server import Server
from channel import Channels
from user import User
from message import Message

argument_parser = ArgumentParser()
argument_parser.add_argument('-f', '--filename', default='server_json.json', help='Chemin du fichier JSON dans lequel les données du serveur sont stockées')
argument_parser.add_argument('-u','--url')
arguments = argument_parser.parse_args()
server : Server
if arguments.filename is not None :
    server = Server.load_from_json_file(arguments.filename)
elif arguments.url is not None :
    server = RemoteServer(arguments.url)
else :
    print('Error, -j or -u should be set')
    exit(-1)

client = Client(server)
#client.accueil()
print(server.get_users())


