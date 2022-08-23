from multiprocessing import context
from django.shortcuts import render, redirect
from multiprocessing import context
from django.shortcuts import render, redirect
# from .models import newBindata

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
    latitude = database.child('/test').child('lattitude').get().val()
    longitude = database.child('/test').child('longitude').get().val()
    # context={
    #     "latitude":latitude,
    #     "longitude":longitude
    # }
    print(latitude)
    print(longitude)
    return render(request, 'home.html', {'latitude':latitude, 'longitude':longitude})



