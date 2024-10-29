from flask import Flask, render_template, request
import pickle
import numpy as np
import streamlit as st

st.write("Hello world")

model = pickle.load(open("iris.pkl","rb"))


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('')

