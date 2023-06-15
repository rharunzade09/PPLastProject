from flask import Flask, render_template
import os
folder = os.getcwd() # запомнили текущую рабочую папку
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder=folder, static_folder=folder)  


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/java')
def java():
    return render_template('java.html')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)