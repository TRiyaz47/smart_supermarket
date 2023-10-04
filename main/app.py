from flask import Flask,render_template,session,request,redirect,url_for,flash


app=Flask(__name__)


@app.route("/")
def home():
    return "This is home page"


if __name__=="__main__":
    app.run(debug=True)
