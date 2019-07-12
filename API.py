import requests
import vulners
import urllib.request
from zipfile import ZipFile

# vulners_api = vulners.Vulners(api_key="CIN1GWJUIOQXYCJHR6RUZQAQNOODULLW40MVENMKMYXTNUDU2CS2J566DTGTDXH1")
# vulners_api.vulners_get_request('https://vulners.com/api/v3/archive/collection/?type=nessus', "type=nessus");
# vulner = vulners_api.archive("nessus")
# req = requests.get(url='https://vulners.com/api/v3/archive/collection/?type=nessus',api_key='CIN1GWJUIOQXYCJHR6RUZQAQNOODULLW40MVENMKMYXTNUDU2CS2J566DTGTDXH1')
# urllib.request.urlretrieve("https://vulners.com/api/v3/archive/collection/?type=nessus", "nessus.zip")
# archive = ZipFile("nessus.zip")
 req = requests.get(
     url='https://vulners.com/api/v3/archive/collection/?type=nessus&apiKey=CIN1GWJUIOQXYCJHR6RUZQAQNOODULLW40MVENMKMYXTNUDU2CS2J566DTGTDXH1')
 print(req)
