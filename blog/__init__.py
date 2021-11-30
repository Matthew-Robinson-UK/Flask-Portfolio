from flask import Flask 

app = Flask(__name__)
app.config['SECRET_KEY'] = '86a13d29b940a84c8c8a067871c226da70397817097eaf3b' 

from blog import routes