from flask import Flask, render_template
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import random
import os 
from flask import Flask, request
from flask import Flask, Response
from flask import send_file, send_from_directory, safe_join, abort
import webbrowser
from docx import Document
from io import StringIO



app = Flask(__name__, static_url_path='/static')




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
       
@app.route('/button', methods=['POST', 'GET'])
def roulette():
    with open("GutProject.doc", "w") as f:
        x = (random.randint(1, 60059))
        text = strip_headers(load_etext(x)).strip()
        f.write(text)
        f.close()
    return send_file('GutProject.doc',
    mimetype='application/msword',
    attachment_filename='GutProject.doc',
    as_attachment=True)
    
       

        
    
    
        

if __name__ == '__main__':
    app.run(debug=True)
