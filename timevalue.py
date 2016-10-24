from flask import Flask
from flask import render_template
from flask import request

import math, locale

app = Flask(__name__)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
	if request.method == 'POST':
		result = get_answer(request.form)
	return render_template('calculate.html', p_init=result['p_init'], p_final=result['p_final'], rate=result['rate'], duration=result['duration'], msg=result['msg']) 

@app.route('/reset')
def reset():
	return render_template('calculate.html') 

def get_answer (form_data):

	locale.setlocale( locale.LC_ALL, '')
	p_init = int(form_data['p_init'])
	rate = float(form_data['rate'])
	real_rate = rate / 100
	duration = int(form_data['duration'])
	p_final = form_data['p_final']

	if p_final is None or p_final == '':
		p_final = p_init * (1 + real_rate)**duration
	if p_init is None:
		p_init = p_final / (1 + real_rate)**duration
	if duration is None:
		duration = (math.log1p(p_final/p_init))/(math.log1p(1+real_rate))
	if rate is None:
		rate = ((p_final/p_init)**(1/duration))	- 1

	p_final = locale.currency(p_final)
	p_init = locale.currency(p_init)
	
	msg = "Investing " + p_init + " for " + str(duration) + " years at an APR of " + str(rate) + "% will result in " + p_final + "." 
	return {'p_init':p_init, 'p_final':p_final, 'rate':rate, 'duration':duration, 'msg':msg}
	
	
	
