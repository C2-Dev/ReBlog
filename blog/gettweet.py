import requests
r = requests.get('https://publish.twitter.com/oembed?url=https://twitter.com/Interior/status/463440424141459456&omit_script=true')
etweet = r.json()
print(etweet['html'])