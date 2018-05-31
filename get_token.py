import requests, json, codecs

url_token = "https://apis.goflipr.com/OAuth2/token"
url_flipr = "https://apis.goflipr.com/modules/FLIPR_ID/survey/last"

payload_token = "grant_type=password&username=USERNAME_ENCODED&password=PASSWORD"
headers_token = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response_token = requests.request("POST", url_token, data=payload_token, headers=headers_token)
jsonlist = json.loads(response_token.text)
jsonlist = jsonlist['access_token']


headers_flipr = {
    'Authorization': "Bearer " + str(jsonlist),
    'Cache-Control': "no-cache",
    }

response_flipr = requests.request("GET", url_flipr, headers=headers_flipr)
payload = response_flipr.text

f = codecs.open('data.txt', 'w', encoding='utf8')
f.write(payload)

