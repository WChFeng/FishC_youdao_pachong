import urllib.request


url = 'http://m.mmjpg.com/mm/1096/2'

req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

a = html.find('img src=')
b = html.find('.jpg', a)

print(html[a+9:b+4])

with open('pic.jpg', 'wb') as f:
    pic_url = 'http://img.mmjpg.com/2017/1096/4.jpg'
    req = urllib.request.Request(pic_url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
    response = urllib.request.urlopen(pic_url)
    html = response.read()
    print(pic_url)
    f.write(html)
# print(html[a+9: b+4])