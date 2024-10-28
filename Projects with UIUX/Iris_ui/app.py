from flask import flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("iris.pkl","rb"))

app = flask(__name__)


@app.route('/')
def home():
    return render_template('')