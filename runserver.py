"""
This script runs the scratchFlaskApp application using a development server.
"""

from os import environ
from scratchFlaskApp import app

#adding firestore files
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore

#cred = credentials.Certificate("scratchFlaskApp/secFolder/secondAuth.json")
#firebase_admin.initialize_app(cred)
#db = firestore.client()

#print("Link success")



if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
