from flask import Flask, render_template, request # import flask
app = Flask(__name__) # create an app instance

@app.route('/')
@app.route('/index')
def home():
    #chosen_mood = request.form['mood']
    return render_template('index.html')
    

@app.route('/length')
def length():
    return render_template('length.html')

"""
@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')
"""
"""app.route('/about')
def about():
    return render_template('about.html')
"""


"""def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query('''SELECT * FROM data''')
    return render_template('index.html')"""

if __name__ == "main":
    app.run(debug=True)

"""To run the web app, in terminal type in:
python moodvie.py 
OR
export FLASK_APP=moodvie.py
flask run

and enter the URL http://localhost:5000/ or
http://127.0.0.1:5000/
"""