# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 00:42:23 2018

@author: Lourenço Neto
"""

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/set')
def setcookie():
    resp = make_response('Setting cookies to tell that you are using a Flask Application!')
    resp.set_cookie('app', 'flask')
    return resp

@app.route('/get')
def getcookie():
    app = request.cookies.get('app')
    return "This application uses " + app

if __name__ == '__main__':
    app.run(debug=True)