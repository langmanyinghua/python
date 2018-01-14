#coding=utf-8
from flask import *
import model

app = Flask(__name__)

@app.route('/')
def root():
	return 'hello python'

@app.errorhandler(404)
def page_not_found(error):
    return jsonify()

@app.route('/get',methods = ['GET'])
def get():
	return jsonify('')


if __name__ == '__main__':
	app.debug = True
	app.config['JSON_AS_ASCII'] = False
	app.run()
