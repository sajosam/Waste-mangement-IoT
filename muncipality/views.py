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

    context={
      "distance":distance,
      "binid":binid,
      "capacity":capacity,
      "muncipality":muncipality,
      "place":place
    }

    return render(request,"bin.html",context)

def single(request):
  distance = database.child('/test').child('distance').get().val()
  id = database.child('/test').child('id').get().val()
  capacity = database.child('/test').child('capacity').get().val()
  if distance > 0 and distance < 3:
    dist=25
  elif distance > 3 and distance < 6:
    dist=45
  elif distance > 6 and distance < 9:
    dist=65
  elif distance > 9 and distance < 12:
    dist=85
  else:
    dist=100
  
  context={
    "distance":distance,
    "id":id,
    "capacity":capacity,
    "dist":dist,
    "place":"demo"
  }
  return render(request, 'single.html', context)


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

