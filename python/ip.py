import urllib.request,json
_url='http://api.ipstack.com/check?access_key=b1a25591364acdaffc213fc8c29fa202&format=1&security=1&hostname=1'
p=''
with urllib.request.urlopen(_url) as response:
   #print(json.loads(response))
   p=response.read()
# for i in p:
# 	print(i)
print(type(p))
