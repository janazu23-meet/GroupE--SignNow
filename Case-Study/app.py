from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDqwuafRhZWB1A7-BOUuTI46Oxgv6Ew9AE",
  "authDomain": "case-study-29a7e.firebaseapp.com",
  "projectId": "case-study-29a7e",
  "storageBucket": "case-study-29a7e.appspot.com",
  "messagingSenderId": "318134472649",
  "appId": "1:318134472649:web:bd6533fbd6c567ba4f6218",
  "measurementId": "G-LFWTBRF4SY",
  "databaseURL": "https://case-study-29a7e-default-rtdb.europe-west1.firebasedatabase.app" 
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "yuggnoijibgyfdrdv"

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)