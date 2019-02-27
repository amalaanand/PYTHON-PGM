from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "Hello...."
@app.route("/home")
def home():
    return "Welcome to my home"
@app.route("/contact")
def contact():
    return "Contact Us:222222"
@app.route("/about")
def about():
    return "SNIT Vadakkevila,Kollam"        

if(__name__=="__main__"):
    app.run()