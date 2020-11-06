"""
action="{{%20url_for('submit')%20}}"

"""
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)

bootstrap = Bootstrap(app)

@app.route("/survey", methods=['GET', 'POST'])
def survey():
    print(request)
    print(request.values)
    print(request.args)
    print(request.form)

    if request.method == "POST":

        profile = {
            "account": request.values.get("Account"),
            "password": request.values.get("Password"),
            "line_user_id": request.values.get("user_ID"),
            "user_name": request.values.get("UserName"),
            "email": request.values.get("UserMail"),
            "phone": request.values.get("Phone"),
            "gender": request.values.get("gender"),
            "age": request.values.get("age"),
            "taste": request.values.getlist("taste"),
            "style": request.values.getlist("taste1"),
            "priority": request.values.getlist("taste2"),
            "other": request.values.get("OtherPriority"),
            "dislike_ingredient": request.values.get("dislike_ingredient")


        }
        print(profile)
        return render_template("sucess.html")
    return render_template("generic.html")

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/table", methods=['GET', 'POST'])
def table():
    return render_template("elements.html")

@app.route("/sucess", methods=['GET', 'POST'])
def sucess():
    return render_template("sucess.html")

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        result = {
            "satisfication": request.values.get("radio")
        }
        print(result)
        return render_template('sucess.html')
    return render_template('feedback.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

# def create_app(config_filename):
#     app = Flask(__name__)
#     app.register_error_handler(404, page_not_found)
#     return app

if __name__ == '__main__':
    app.run(port=8080, debug=True) #host='0.0.0.0',