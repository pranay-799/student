from flask import Flask, request, send_file, render_template
from generate import generate_image
from io import BytesIO

@app.route('/')
def home():
    return render_template('index.html')