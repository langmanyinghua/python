#coding=utf-8;
import requests;

result = requests.post("http://192.168.31.86:8082/manager/assist/update")
print result.content;