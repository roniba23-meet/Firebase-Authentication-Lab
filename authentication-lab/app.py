from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDqqDT5aqpqERyVf_LIC_eS4mmRcozoErE",
  "authDomain": "first-lab-demo.firebaseapp.com",
  "projectId": "first-lab-demo",
  "storageBucket": "first-lab-demo.appspot.com",
  "messagingSenderId": "691046391016",
  "appId": "1:691046391016:web:caa31f97409ff158e2bd5d",
  "measurementId": "G-G4YL307S83"
}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signup.html")




@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signin.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)