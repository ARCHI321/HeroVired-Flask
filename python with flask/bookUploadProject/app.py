
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

@app.route('/delete', methods=['POST'])
def delete_value():
    value_to_delete = request.form['value']
    print("1",value_to_delete)
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM flask.book WHERE id=%s',(value_to_delete,));
    mysql.connection.commit()
    # cursor.execute('SELECT * FROM flask.book')
    # rows = cursor.fetchall()
    # print(rows)
    # cursor.close()
    return redirect(url_for('book'))

@app.route("/book",methods=['GET','POST'])
def book():
    rows = 0
    cursor=0
    #check if the request methosd is POST
    if request.method=='POST' and 'bookName' in request.form and 'authorName' in request.form and 'publishedDate' in request.form:
        BOOKNAME=request.form['bookName']
        AUTHORNAME=request.form['authorName']
        PUBLISHEDDATE=request.form['publishedDate']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO flask.book (bookName,authorName,publishDate) VALUES (%s , %s , %s)',(BOOKNAME,AUTHORNAME,PUBLISHEDDATE))
        mysql.connection.commit()

        cursor.execute('SELECT * FROM flask.book')
        rows = cursor.fetchall()
        print(book)


        return render_template('book.html', bookAndAuthor = rows)
    print("hello")
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM flask.book')
    rows = cursor.fetchall()
    return render_template('book.html', bookAndAuthor = rows)

if __name__=='__main__':
    app.run(debug=True)