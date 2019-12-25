#temp file for learning purposes
from app import app

@app.route('/')
@app.route('/index') #both '/' and '/index' will link to the following:
def index():
    user = {'username': 'Mockey'} #mock user
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user) #collecting webpage from html template
