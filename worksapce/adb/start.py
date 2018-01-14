#coding=utf-8
from uiautomator import device as d
import time

print d.info

def open_wx():
	#屏幕亮起
	d.screen.on()
	#回到桌面
	#d.press.home()
	d(text = "微信").click()
	time.sleep(3)
	d.click(570,100)


open_wx()

