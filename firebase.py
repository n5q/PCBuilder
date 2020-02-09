import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-adminsdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pcbuilder-nsq.firebaseio.com/'
})

