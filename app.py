#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os
import qrcode
from bs4 import BeautifulSoup

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # scrape target website and fill in form fields
        # submit form using Requests library
        return 'Form submitted successfully!'
    else:
        # generate QR code image
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data('http://192.168.4.113:8001/auto311')
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('static/qr_code.png')
        return render_template('index.html')
    return render_template('pages/placeholder.home.html')


@app.route('/auto311')
def auto311():
    


    return render_template('pages/placeholder.about.html')




#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=8001)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
