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


def new(request):
    id = database.child('/').child('id').get().val()
    name = database.child('/').child('name').get().val()
    new = database.child('/').child('new').get().val()
    print(id, name, new)
    return render(request,"new.html",{"id":id,"name":name,"new":new })



# <script type="module">
#   // Import the functions you need from the SDKs you need
#   import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.2/firebase-app.js";
#   // TODO: Add SDKs for Firebase products that you want to use
#   // https://firebase.google.com/docs/web/setup#available-libraries

#   // Your web app's Firebase configuration
#   const firebaseConfig = {
#     apiKey: "AIzaSyA1TcaRA5_EsbY0wdms3HP7wtxwGS67Ubc",
#     authDomain: "demodjango-d70d8.firebaseapp.com",
#     projectId: "demodjango-d70d8",
#     storageBucket: "demodjango-d70d8.appspot.com",
#     messagingSenderId: "853786892493",
#     appId: "1:853786892493:web:986bfce5f930cc72edb184"
#   };

#   // Initialize Firebase
#   const app = initializeApp(firebaseConfig);
# </script>

# ERROR: pyrebase4 4.5.0 has requirement gcloud>=0.18.3, but you'll have gcloud 0.17.0 which is incompatible.
# ERROR: pyrebase4 4.5.0 has requirement oauth2client>=4.1.2, but you'll have oauth2client 3.0.0 which is incompatible. 
# ERROR: pyrebase4 4.5.0 has requirement pycryptodome>=3.6.4, but you'll have pycryptodome 3.4.3 which is incompatible. 
# ERROR: pyrebase4 4.5.0 has requirement requests>=2.19.1, but you'll have requests 2.11.1 which is incompatible.       
# ERROR: pyrebase4 4.5.0 has requirement requests-toolbelt>=0.7.1, but you'll have requests-toolbelt 0.7.0 which is incompatible.