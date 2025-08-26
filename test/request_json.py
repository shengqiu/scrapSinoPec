import requests
import json


url = "https://ec.sinopec.com/f/supp/bid/queryInquiryotices.do?paramJson=%7B%7D"
payload = {
    'pageNo': '1',
    'type': '150'
}
headers = {
  'Cookie': 'JSESSIONID=1A8BDFEDD38F947419EC2E86D17489FA; SERVERID=7c87ef910d16daea198140372adca059|1756190655|1756190655; seid=1A8BDFEDD38F947419EC2E86D17489FA; sevIp=247',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
}
response = requests.post(url, headers=headers, data=payload)
data = json.loads(response.text)['result']['result']
print(data)