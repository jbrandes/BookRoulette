from flask import Flask, render_template
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import random
import os 
from flask import Flask, request
from flask import Flask, Response
from flask import send_file, send_from_directory, safe_join, abort



app = Flask(__name__, static_url_path='/static')



@app.route('/')
def home():
    render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
       
@app.route('/button', methods=['POST', 'GET'])
def roulette():
    f = open("GutProject.txt", "w")
    for x in range(1):
        y = (random.randint(0, 59000))
        text = strip_headers(load_etext(y)).strip()
        f.write(text)
        pass
        
    
    
        

if __name__ == '__main__':
    app.run(debug=True)
