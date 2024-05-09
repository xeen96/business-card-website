import os
from flask import Flask, render_template, send_from_directory, redirect, url_for, send_file
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('base.html', title="Home", selected_button="home")
        
@app.route('/whoiam')
def who_i_am():
    current_year = datetime.datetime.now().year   #AGE CALCULATION 
    age = current_year
    return render_template('base.html', title="Who I Am", selected_button="who_i_am", age = age)

@app.route('/skills')
def what_i_do():
    return render_template('base.html', title="Skills", selected_button="skills")

@app.route('/contact')
def contact():
    return render_template('base.html', title="Contact", selected_button="contact")


@app.route('/static/<path:path>')
def image(path):
    return send_from_directory('static', path)

@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory('styles', filename)

@app.route('/download-cv')
def download_cv():
    app_root = os.path.dirname(os.path.abspath(__file__))
    cv_path = os.path.join(app_root, 'cv/your_cv.pdf') #PATH TO YOUR CV
    return send_file(cv_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True) #running app in debug mode

