from flask import Flask, render_template
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import random

 f = open("GutProject.txt", "w")
    for x in range(1):
        y = (random.randint(0, 100))
        text = strip_headers(load_etext(y)).strip()
        f.write(text)
        
