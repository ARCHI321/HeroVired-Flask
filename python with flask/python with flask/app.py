
from flask import Flask, request, render_template, redirect,url_for,session
from flask_mysqldb import MySQL


app=Flask (__name__)#wsgi application/flask application

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'archisman'
app.config['MYSQL_SCHEMA'] = 'flask'

mysql = MySQL(app)

app.secret_key = 'my_secret_key'


@app.route("/")
def home():
    return "Welcome to project"


@app.route("/login",methods=['GET','POST'])
def login():
    #check if the request methosd is POST
    if request.method=='POST' and 'name' in request.form and 'password' in request.form:
        #extract the values
        # NAME=request.form.get('name')
        # EMAIL=request.form.get('email')
        NAME=request.form['name']
        PASSWORD=request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM flask.user WHERE username=%s AND password=%s',(NAME,PASSWORD))
        user = cursor.fetchone()#in form of a tuple

        if user:
            session['loggedin'] = True
            session['username'] = user[1]
            session['password'] = user[2]
            return 'login successful'
        else:
            return 'login failed'


    return render_template('login.html')
@app.route("/register",methods=['GET','POST'])
def register():
    #check if the request methosd is POST
    if request.method=='POST' and 'name' in request.form and 'password' in request.form:
        #extract the values
        # NAME=request.form.get('name')
        # EMAIL=request.form.get('email')
        NAME=request.form['name']
        PASSWORD=request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO flask.user (username,password) VALUES (%s , %s)',(NAME,PASSWORD))
        mysql.connection.commit()


        return 'Successful Registration'


    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True)