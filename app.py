from flask import Flask, render_template
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import random
import os 
from flask import send_from_directory




bookroulette = Flask(__name__, static_url_path='/static')





@bookroulette.route('/')
def welcome():
    return 'Welcome to the server'

@bookroulette.route('/books')
def books():
    return render_template("main.html")

@bookroulette.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
       
@bookroulette.route('/roulette', methods=['POST', 'GET'])
def roulette():
    f = open("GutProject.txt", "w")
    for x in range(1):
        y = (random.randint(0, 59000))
        text = strip_headers(load_etext(y)).strip()
        f.write(text)
        return render_template("main.html")
       

if __name__ == "__main__":
    bookroulette.run(debug=True)
