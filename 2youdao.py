import urllib.request
import urllib.parse
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

data = {
        'i': '你是谁？',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1504696330827',
        'sign': '5ff3a4e12540d3430431b4de9fbe00c3',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'true',
}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)