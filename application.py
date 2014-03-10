from flask import Flask, redirect, url_for, render_template
 
application = Flask(__name__, 
	static_url_path='',
	static_folder='',
	template_folder='html')
 
@application.route('/')
def hello_world():
    return render_template('index.html')
 
if __name__ == '__main__':
    application.run()