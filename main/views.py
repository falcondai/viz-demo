from main import app
from flask import render_template, abort

# graph dimensions
width = 900
height = 500

@app.route('/')
def index():
	return render_template('index.html', width=width, height=height)
	
@app.route('/graph/<dataset>')
def graph(dataset):
	if dataset == 'wholeyear':
		return render_template('graph.html', dataset=dataset, freq='daily', order_header='fullperiod', freq_header='counttime', axis_format='%b', tt_format='%x', width=width, height=height)
	elif dataset == 'benghazi':
		return render_template('graph.html', dataset=dataset, freq='hour', order_header='series2', freq_header='Freq', axis_format='%m/%d %H', tt_format='%x %X', width=width, height=height)
	elif dataset == '47percent':
		return render_template('graph.html', dataset=dataset, freq='hour', order_header='series2', freq_header='Freq', axis_format='%m/%d %H', tt_format='%x %X', width=width, height=height)
	else:
		abort(404)