import requests
url='http://www.lottery.gov.cn/historykj/history.jspx?_ltype=dlt'
req = requests.get(url)
print(req.text)