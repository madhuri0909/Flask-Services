import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Home Page<h1>"


@app.route('/hello/<name>')
def hello_name(name):
   x=json.loads(name)
   incNumber=x['incident']
   description=x['description']
   state=x['state']
   region=x['region']
   opentime=x['opentime']
   return render_template('home.html', incident = incNumber, state=state, market=region, description=description, opentime=opentime)


def about():
    return "<h1>About Page<h1>"
if __name__ == '__main__':
        app.run(debug=True)