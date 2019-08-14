from flask import Flask, render_template
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import random
import os 
from flask import send_from_directory
import boto3
from flask import Flask, request
from flask import Flask, Response
from boto3 import client
import botocore
from boto.s3.key import Key



app = Flask(__name__, static_url_path='/static')


def get_client():
    return client(
        's3',
        'us-east-1',
        aws_access_key_id='AKIAT2WU5IJC57E53KM6',
        aws_secret_access_key='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'
    )




@app.route('/')
def welcome():
    return 'Welcome to the server'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
       
@app.route('/roulette', methods=['POST', 'GET'])
def roulette():
    s3 = get_client()
    f = open("GutProject.txt", "w")
    for x in range(1):
        y = (random.randint(0, 59000))
        text = strip_headers(load_etext(y)).strip()
        book = f.write(text)
        client = boto3.client('s3')
        response = client.put_object( 
           Bucket='book-roulette',
           Body='book',
           Key='files/GutProject.txt')
           return Response(
               file['Body'].read(),
               mimetype='text/plain',
               headers={"Content-Disposition": "attachment;filename=GutProject.txt"}
    )
        
        

if __name__ == '__main__':
    app.run(debug=True)
