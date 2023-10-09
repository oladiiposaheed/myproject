import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
binfo = response.json() #converting json string to python dict
print(type(binfo))
print(binfo)
#print('Bit coin price as on:', binfo['time'])
print('Bit coin price as on:', binfo['time']['updated'])
print()
print('1 Bit Coin as at {}: ${}'.format(binfo['time']['updateduk'], binfo['bpi']['USD']['rate']))
print()
print('1 Bit Coin as at {} in {}: £{}'.format(binfo['time']['updateduk'], binfo['bpi']['EUR']['symbol'], binfo['bpi']['EUR']['rate']))
