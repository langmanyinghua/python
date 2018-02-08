#coding=utf-8
from fabric.api import *

env.user = 'root'
env.hosts = [
   '192.168.31.101'
]

env.password = '123456'

def test_one():
	run('cat /etc/issue')