from flask import Flask , jsonify , render_template , request
from flask_cors import CORS , cross_origin
import os

app=Flask(__name__)
CORS(app)

