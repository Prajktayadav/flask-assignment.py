from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from hashlib import sha256
import config
import certifi
import uuid

app = Flask(__name__)
app.config.from_object(config)

client = MongoClient(config.MONGO_URI,tlsCAFile=certifi.where())
db = client["Userdatabase"]
col = db["users"]

@app.route('/')
def index():
    return redirect(url_for('login'))