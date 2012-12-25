from main import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/graph')
def graph():
	return render_template('graph.html')
