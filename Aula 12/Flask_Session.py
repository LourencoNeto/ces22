# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 01:19:00 2018

@author: Lourenço Neto
"""

from flask import Flask, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    session['user'] = 'Lourenço'
    return 'Save the name of the user'

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    
    return 'It is not logged in' 

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'The last user is not listed now as active'

if __name__ == '__main__':
    app.run(debug=True)