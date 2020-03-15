"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from scratchFlaskApp import app

#adding firestore files
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from scratchFlaskApp import URPlanClasses
from scratchFlaskApp.URPlanClasses import Class

cred = credentials.Certificate("scratchFlaskApp/secFolder/secondAuth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#print("Link success")

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    doc_refClass = db.collection(u'classes').document(u'53095')
    try:
        docClass = doc_refClass.get()
        classQuery = Class.from_dict(docClass.to_dict())
        #print(classQuery)
    except google.cloud.exceptions.NotFound:
        print("Document Not Found")


    testMessage = classQuery.courseName

    #return render_template(
    #    'contact.html',
    #    title='Contact',
    #    year=datetime.now().year,
    #    message='Your contact page.'
    #)
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message=testMessage
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
