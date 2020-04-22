from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

# @app.route('/recommendations')
# def recommendations():

# if __name__ == 'main'
    #app.run()