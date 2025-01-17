import os
import json
# The capital F indicates that this is a class.
# Instead of writing HTML tags inside the Python file, we can use render_template.
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# Create an instance of the Flask class.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Telling Flask which URL triggers the function.
# A decorator starts with @, which is also called pie notation.
# A decorator is a way of wrapping functions.
@app.route("/")
def index():
    # Flask will look for the 'templates' folder to find the HTML file we referenced in parentheses.
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    #we need to oopen the file for python to read it
    #r means read only
    #python will open jason file as read only
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact") #it is good practice to use _ when you are naming a variable


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# Ensure there are two blank lines between functions for PEP8 compliance.
if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
