from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sports', methods=['GET'])
def sports():
    return render_template('sports.html')


@app.route('/technology', methods=['GET'])
def technology():
    return render_template('technology.html')


@app.route('/politics', methods=['GET'])
def politics():
    return render_template('politics.html')


@app.route('/business', methods=['GET'])
def business():
    return render_template('business.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)

