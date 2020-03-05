#Initializes the neccessary configuration to link to firebase session
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("") #add your credential .json file in "" to enable admin login functionality.

default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

print("FirebaseAdmin link successful")
print(default_app.name)