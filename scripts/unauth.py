from flask import Flask, render_template, redirect, url_for
#from energenie import switch_on, switch_off
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on/')
def on():
    subprocess.Popen(['/usr/bin/env', 'python', 'open.py'], subprocess.PIPE)
    #app.r('/off/')
    return redirect(url_for('index'))

@app.route('/off/')
def off():
    #switch_off()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
