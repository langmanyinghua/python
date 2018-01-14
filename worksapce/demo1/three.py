#coding=utf-8

def one():
	print 'one'
	two()

def two():
	print 'two'

one()

env = 'prod-hg'

cmd_crawler = 'nohup java -jar crawler.jar --spring.profiles.active=%s &' % (env)
print cmd_crawler