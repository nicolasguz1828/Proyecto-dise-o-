from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/procedimiento')
def procedimiento():
    return render_template('procedimiento.html')

@app.route('/analisis')
def analisis():
    return render_template('analisis.html')  

@app.route('/VC')
def vc():
    return render_template('vc.html')

@app.route('/IC')
def ic():
    return render_template('ic.html')

@app.route('/TLC')
def tlc():
    return render_template('tlc.html')

@app.route('/FRC')
def frc():
    return render_template('frc.html')

if __name__ == '__main__':
    app.run(debug=True)    

