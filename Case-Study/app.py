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

whyus = {"name": "Why Us?", "information": ["A combination of technology and human touch as it relates to sign language translation. Sign language translation is one of the only domains in which the human touch is more important than the related technology", "Accessible user experience for all categories of deaf persons: elderly, deaf and blind and more. Minimum clicks involved", "One stop shop - everything the deaf community needs in one place", "Minimum bureaucracy. We wish we could switch 'Minimum' to 'zero'", "Free for deaf users - Thanks to our B2B&B2G business models", "All sign languages - We connect local deaf people with local interpreters"]}

@app.route('/')
def index():
	return render_template('index.html', whyus=why_us)

@app.route('/blog')
def blog():
  return render_template('blog.html')

@app.route('/portfolio-details')
def portfolio-details():
  return render_template('portfolio-details.html')

@app.route('/blog-single')
def blog-single():
  return render_template('blog-single.html')

@app.route('/inner-page')
def inner-page():
  return render_template('inner-page.html')

if __name__ == '__main__':
	app.run(debug=True)