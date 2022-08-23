from multiprocessing import context
from django.shortcuts import render, redirect
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import newBindata

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

def bin(request):
    distance = database.child('/test').child('distance').get().val()
    binid= database.child('/test').child('binid').get().val()
    capacity = database.child('/test').child('capacity').get().val()
    muncipality = database.child('/test').child('muncipality').get().val()
    place = database.child('/test').child('place').get().val()
    if distance > 0 and distance < 4:
        dist=100
    elif distance > 4 and distance < 8:
        dist=85
    elif distance > 8 and distance < 10:
        dist=65
    elif distance > 10 and distance < 12:
        dist=45
    else:
        dist=25

    context={
      "distance":distance,
      "binid":binid,
      "capacity":capacity,
      "muncipality":muncipality,
      "place":place,
        "dist":dist
    }

    return render(request,'bin.html',context)



def createbin(request):
  if request.method == 'POST':
      # distance = request.POST['distance']
    binid = request.POST['binid']
    capacity = request.POST['capacity']
    muncipality = request.POST['muncipality']
    place = request.POST['place']
      # push value to _db
    distance=0.0
    latitude=0.0
    longitude=0.0
    
    # database.child('test').child('distance').set(distance)
    # database.child('test').child('binid').set(binid)
    # database.child('test').child('capacity').set(capacity)
    # database.child('test').child('muncipality').set(muncipality)
    # database.child('test').child('place').set(place)
    # insert data to BIn db
    newBindata.objects.create(Binid=binid, capacity=capacity, muncipality=muncipality, place=place, latitude=latitude, longitude=longitude)
    return redirect('bin')

  return render(request, 'createbin.html')

