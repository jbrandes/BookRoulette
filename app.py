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
       
@app.route('/download', methods=['POST'])
def download():
    with open("GutProject.doc", "w") as f:
        x = (random.randint(1, 60059))
        text = strip_headers(load_etext(x)).strip()
        f.write(text)
        f.close()
    return send_file('GutProject.doc',
    mimetype='application/msword',
    attachment_filename='GutProject.doc',
    as_attachment=True)
       
@app.route('/tab', methods=['POST'])
def tab():
    with open("BookRoulette.html", "w") as f:
        x = (random.randint(1, 60059))
        book = strip_headers(load_etext(x)).strip()
        f.write(book)
        f.close
        filename = 'file:///'+os.getcwd()+'/' + 'BookRoulette.html'
        webbrowser.open_new_tab(filename)
        return render_template('BookRoulette.html')
        
       


        

if __name__ == '__main__':
    app.run(debug=True)
