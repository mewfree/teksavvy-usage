import requests

APIKEY = 'YOUR-API-KEY-HERE'
CAP = 'YOUR-DATA-CAP-HERE'

r = requests.get('https://api.teksavvy.com/web/Usage/UsageSummaryRecords?$filter=IsCurrent%20eq%20true', headers={'TekSavvy-APIKEY': APIKEY})

d = r.json()['value'][0]
pd = d['OnPeakDownload']
left = CAP - pd

s = 'You have used '+str(pd)+'GB out of your '+str(CAP)+'GB limit'
s += ' ('+str(left)+'GB left)'
print(s)
