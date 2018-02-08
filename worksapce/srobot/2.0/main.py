#coding=utf-8
import deploy,process
import threading,time

#皇冠集团配置文件
def get_config_hg():
	config = {
		'env'			:	'prod-hg',
		'crawler_url'	:	'',#http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v2/crawler-1.0-SNAPSHOT.jar
		'manager_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v2/manager-1.0-SNAPSHOT.jar',#
		'server_url'	:	'',#http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v2/server-1.0-SNAPSHOT.jar
		'web_url'		:	'',
		'html_url'		:	'',#http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v2/admin.zip
		'server'		:	[
			{
				'hostname'	:	'139.196.105.242',
				'username'	:	'root',
				'password'	:	'jkh#49@kzNeO1&efzN'
			},
			{
				'hostname'	:	'139.196.106.42',
				'username'	:	'root',
				'password'	:	'jkh#49@kzNeO1&efzN'
			},
			{
				'hostname'	:	'139.196.104.118',
				'username'	:	'root',
				'password'	:	'jkh#49@kzNeO1&efzN'
			},
			{
				'hostname'	:	'139.196.106.110',
				'username'	:	'root',
				'password'	:	'jkh#49@kzNeO1&efzN'
			}
		]
	}
	return config

#第一网销配置文件
def get_config_dywx():
	config = {
		'env'			:	'prod-dywx',
		'crawler_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v1/crawler-1.0-SNAPSHOT.jar',
		'manager_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v1/manager-1.0-SNAPSHOT.jar',
		'server_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v1/server-1.0-SNAPSHOT.jar',
		'web_url'		:	'',
		'html_url'		:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/resources/v1/admin.zip',
		'server'		:	[
			{
				'hostname'	:	'139.196.141.252',
				'username'	:	'root',
				'password'	:	'Ontouch1310'
			}
		]
	}
	return config

#招商银行配置文件
def get_config_cmb():
	config = {
		'env'			:	'prod',
		'crawler_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/crawler-1.0-SNAPSHOT.jar',
		'manager_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/manager-1.0-SNAPSHOT.jar',
		'server_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/server-1.0-SNAPSHOT.jar',
		'web_url'		:	'',
		'html_url'		:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/admin.zip',
		'server'		:	[
			{
				'hostname'	:	'47.97.6.188',
				'username'	:	'root',
				'password'	:	'Qiadao123'
			}
		]
	}
	return config

#演示平台配置文件
def get_config_show():
	config = {
		'env'			:	'prod-show',
		'crawler_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/crawler-1.0-SNAPSHOT.jar',
		'manager_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/manager-1.0-SNAPSHOT.jar',
		'server_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/server-1.0-SNAPSHOT.jar',
		'web_url'		:	'',
		'html_url'		:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v6/admin.zip',
		'server'		:	[
			{
				'hostname'	:	'118.178.95.100',
				'username'	:	'root',
				'password'	:	'Qiadao123'
			}
		]
	}
	return config

#测试配置文件
def get_config_test():
	config = {
		'env'			:	'dev',
		'crawler_url'	:	'',#http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v5/crawler-1.0-SNAPSHOT.jar
		'manager_url'	:	'',#http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v5/manager-1.0-SNAPSHOT.jar
		'server_url'	:	'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v5/server-1.0-SNAPSHOT.jar',
		'web_url'		:	'',
		'html_url'		:	'http://qiadao-test.oss-cn-shanghai.aliyuncs.com/vue/admin.zip',
		'server'		:	[
			{
				'hostname'	:	'139.196.141.252',
				'username'	:	'root',
				'password'	:	'Qiadao123'
			}
		]
	}
	return config

#开始执行
def main():
	config = get_config_hg()
	#初始化服务器
	#deploy.main(config)
	#更新服务器
	process.main(config)

main()
