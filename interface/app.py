from flask import Flask , render_template

app = Flask(__name__)

posts = [
    {
        'title': 'ITCK',
        'author': 'Rohullah',
        'content': 'this is a test',
        'data_posted': 'April 18, 2023'
    },
    {
        'title': 'Lab',
        'author': 'hasib',
        'content': 'this is a test2',
        'data_posted': 'April 19, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts ,title='home page')

@app.route('/about')
def about():
    return render_template('about.html', title='about page')

if __name__ == '__main__':
    app.run(debug=True)