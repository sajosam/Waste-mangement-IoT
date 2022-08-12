from django.shortcuts import render

import pyrebase
 
Config = {
  "apiKey": "AIzaSyA1TcaRA5_EsbY0wdms3HP7wtxwGS67Ubc",
  "authDomain": "demodjango-d70d8.firebaseapp.com",
  "databaseURL": "https://demodjango-d70d8-default-rtdb.firebaseio.com",
  "projectId": "demodjango-d70d8",
  "storageBucket": "demodjango-d70d8.appspot.com",
  "messagingSenderId": "853786892493",
  "appId": "1:853786892493:web:986bfce5f930cc72edb184"
}


firebase=pyrebase.initialize_app(Config)
authe = firebase.auth()
database=firebase.database()

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'createbin.html')


def bin(request):
    distance = database.child('/test').child('distance').get().val()
    id = database.child('/test').child('id').get().val()
    capacity = database.child('/test').child('capacity').get().val()

    return render(request,"bin.html",{"distance":distance,"id":id,"capacity":capacity, "place":"demo"})

def single(request):
    return render(request, 'single.html')

