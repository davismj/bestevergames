from flask import Flask, redirect, url_for, render_template
 
application = Flask(__name__, 
	static_url_path='/static',
	static_folder='static',
	template_folder='static/html')
 
@application.route('/')
def hello_world():
    return render_template('index.html')
 
if __name__ == '__main__':
    application.run(debug=True)