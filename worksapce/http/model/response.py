#coding=utf-8

class Response:
	"""docstring for Response"""
	def __init__(self, status = 0, result = '', message = 'ok'):
		self.status = status
		self.result = result
		self.message = message


