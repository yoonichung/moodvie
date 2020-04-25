from flask import Flask, render_template, request # import flask
import sys
app = Flask(__name__) # create an app instance

""" Navigation """
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recommendations')
@app.route('/recommendations')
def reccom():
    return render_template('recomm.html')

"""Options"""
@app.route('/length')
def choose_mood():
    mood = request.args.get("mood")
    print(mood, file=sys.stderr)
    return render_template('length.html',selectedMood=mood)

@app.route('/type')
def choose_length():
    mood = request.args.get("mood")
    length = request.args.get("length")
    return render_template('type.html',selectedMood=mood, selectedLength=length)  

@app.route('/genre')
def choose_type():
    mood = request.args.get("mood")
    length = request.args.get("length")
    type = request.args.get("type")
    return render_template('genre.html',selectedMood=mood, selectedLength=length, selectedType=type)  
#print(mood, file=sys.stderr)

@app.route('/movie')
def choose_movie():
    mood = request.args.get("mood")
    length = request.args.get("length")
    type = request.args.get("type")
    genre = request.args.get("genre")
    return render_template('movie.html',selectedMood=mood, selectedLength=length, selectedType=type, selectedGenre=genre)

""" @app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

app.route('/about')
def about():
    return render_template('about.html')


def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM data''')
    return render_template('index.html') """

if __name__ == "main":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD']=True

"""
To run the web app on mac, in terminal type in:
"python moodvie.py"
OR if using a virtual environment
"source 'name of your environment'/bin/activate"
"export FLASK_APP=moodvie.py" OR "export FLASK_ENV=development" to be in the debug mode
"flask run"

and enter the URL http://localhost:5000/ or
http://127.0.0.1:5000/
"""