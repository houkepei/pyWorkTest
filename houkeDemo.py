import urllib.request

response = urllib.request.urlopen("https://blog.csdn.net/C_J33/article/details/80737053")
buff = response.read()
html = buff.decode("utf8")
# print(response)
# print(buff)
print("----------------------------")
print(html)
