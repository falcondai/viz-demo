from main import app
from flask import render_template, abort

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/graph/<dataset>')
def graph(dataset):
	if dataset == 'wholeyear':
		return render_template('graph.html', dataset=dataset, freq='daily', order_header='fullperiod', freq_header='counttime', axis_format='%b', tt_format='%x')
	elif dataset == 'benghazi':
		return render_template('graph.html', dataset=dataset, freq='hour', order_header='series2', freq_header='Freq', axis_format='%m/%d %H', tt_format='%x %X')
	elif dataset == '47percent':
		return render_template('graph.html', dataset=dataset, freq='hour', order_header='series2', freq_header='Freq', axis_format='%m/%d %H', tt_format='%x %X')
	else:
		abort(404)