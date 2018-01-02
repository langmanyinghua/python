#coding=utf-8
import requests
from pyquery import PyQuery as pq
from wordcloud import WordCloud , ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread



url = 'http://blog.csdn.net/forezp'

#下载html
def download(url):
	if url == None:
		return None
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
		}
		response = requests.get(url,headers = headers)
		if response.status_code == 200:
			return response.content
		else:
			return None
	except Exception as e:
		print e
		return None

#筛选数据
def screen_data():
	html = download(url)
	doc = pq(html)
	titlelist = doc('div.article_title span.link_title a')
	result = ''
	for title in titlelist:
		result = result +" "+pq(title).text()

	descriptionlist = doc('div.article_description')
	for description in descriptionlist:
		result = result +" "+pq(description).text()
	return result

#生成云图
def build_wordcloud():
	text = screen_data()

	font = 'font/DroidSansFallback.ttf'
	mask = imread('image/2.png')
	wordcloud = WordCloud(font_path = font, mask = mask,
		max_words = 2000, background_color = 'white',scale = 1.5,
		max_font_size = 60,random_state = 42,margin = 2)
	wordcloud.generate(text)

	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()

	wordcloud.to_file('new/test.jpg')

build_wordcloud()



