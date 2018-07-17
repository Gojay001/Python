import requests

def getHtmlText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent.encoding
		return r.text
	except:
		return "Exception!"

if __name__ == "__main__":
	url = "http://www.baidu.com"
	print(getHtmlText(url))