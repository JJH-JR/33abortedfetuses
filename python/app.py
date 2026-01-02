from flask import Flask, redirect,url_for,render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from stored_chats import chats

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecret"
### {%...%} for condtiosn or for loops or such
### {{...}} expressions to print output
### {#...#} is for comments



new_input = ""

@app.route('/', methods=["GET","POST"])
def index():
    new_input = request.form.get('input')
    chats.append(new_input)
    ###### if stuff == "help"
    return render_template('index.html', template_chats=chats)

@app.route('/<web_face>')
def about(web_face):
    if web_face == "about":
        return render_template('about.html')
    elif web_face == "settings":
        return render_template('settings.html')
    elif web_face == "chats":
        return render_template('chats.html')
    elif web_face == "profile":
        return render_template('profile.html')
    else:
        return "<h1> idk that one bruh </h1>"




if __name__ == '__main__':
    app.run(debug=True)
    

### Bot Algorythm 
