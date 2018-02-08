#coding=utf-8
import ansible
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase

class ResultCallback(CallbackBase):
	"""docstring for ResultCallback"""
	def __init__(self, arg):
		super(ResultCallback, self).__init__()
		self.arg = arg
		