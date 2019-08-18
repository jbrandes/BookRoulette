from flask import Flask, render_template
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import random
import os 
from flask import Flask, request
from flask import Flask, Response
from flask import send_file, send_from_directory, safe_join, abort
import webbrowser



app = Flask(__name__, static_url_path='/static')




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
       
@app.route('/button', methods=['POST', 'GET'])
def roulette():
    with open("GutProject.txt", "w") as f:
        x = (random.randint(1, 5900))
        text = strip_headers(load_etext(x)).strip()
        f.write(text)
        f.close()
    return send_file('GutProject.txt',
    mimetype='text/plain',
    attachment_filename='GutProject.txt',
    as_attachment=True)
    
