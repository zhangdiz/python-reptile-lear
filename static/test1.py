import urllib.parse
import urllib.request
import urllib.error
import socket

# response = urllib.request.urlopen('http://www.baidu.com')

# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# print(data)

# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('请求超时')

# response = urllib.request.urlopen('http://www.eimoney.com/wall/#/home')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader("server"))

# request = urllib.request.Request('http://www.eimoney.com/wall/#/home')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# from urllib import request, parse

# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'zhangdi'
# };
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)

# print(response.read().decode('utf-8'))

# from urllib import request, parse

# url = 'http://httpbin.org/post'
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# import urllib.request

# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

# import http.cookiejar, urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# import http.cookiejar, urllib.request
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.eimoney.com/wall/#/home')
# cookie.save(ignore_discard=True, ignore_expires=True)

# import http.cookiejar, urllib.request
# filename = 'cookie1.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True) 

# import http.cookiejar, urllib.request
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# from urllib import request,error

# try:
#     response = request.urlopen("http://pythonsite.com/1111.html")
# except error.URLError as e:
#     print(e.reason)
# from urllib import request,error
# try:
#     response = request.urlopen("http://pythonsite.com/1111.html")
# except error.HTTPError as e:
#     print(e.reason)
#     print(e.code)
#     print(e.headers)
# except error.URLError as e:
#     print(e.reason)

# else:
#     print("reqeust successfully")
# import socket

# from urllib import error,request

# try:
#     response = request.urlopen("http://www.pythonsite.com/",timeout=0.001)
# except error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason,socket.timeout):
#         print("time out")

# from urllib.parse import urlparse

# result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# print(result)

# from urllib.parse import urlunparse

# data = ['http','www.baidu.com','index.html','user','a=123','commit']
# print(urlunparse(data))

# from urllib.parse import urljoin

# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))

from urllib.parse import urlencode

params = {
    "name":"zhangdi",
    "age":23,
}
base_url = "http://www.baidu.com?"

url = base_url+urlencode(params)
print(url)