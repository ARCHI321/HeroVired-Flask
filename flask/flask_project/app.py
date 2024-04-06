# from flask import Flask, request, render_template


# app=Flask (__name__)#wsgi application/flask application
# #route handling
# # @app.route("/")
# # def home():
# #     return 'Hello Python FLASK aPPLICATION'
# @app.route("/")
# @app.route("/contact",methods=['GET','POST'])
# def contact():
#     #check if the request methosd is POST
#     if request.method=='POST':
#     #RETRIEVE THEE DATA
#         NAME=request.form.get('name')
#         EMAIL=request.form.get('email')
#         message=request.form.get("message")
#     #RENDER THE TEMPLATE WITH THE DATA
#         return f'thank you,{NAME},for your message: {message}.We will contact you at {EMAIL}'
#     #if the request method is GET(intial page load),render the html page/template
#     return render_template('contact_form.html',name = NAME,email=EMAIL)
# if __name__=='__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template


app=Flask (__name__)#wsgi application/flask application
@app.route("/",methods=['GET','POST'])
def index():
    #check if the request methosd is POST
    if request.method=='POST':
        NAME=request.form.get('name')
        EMAIL=request.form.get('email')
        message=request.form.get("message")
        return render_template('contact_form.html',name=NAME,email=EMAIL)
    return render_template('contact_form.html')
if __name__=='__main__':
    app.run(debug=True)