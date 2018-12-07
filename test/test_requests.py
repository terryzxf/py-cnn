import requests as rqst



url = 'http://172.74.252.58/trakcarelive/trak/web/csp/logon.csp'

keywords = {
    'USERNAME':'0011164',
    'PASSWORD':'983070-'
}

r= rqst.post(url,data=keywords)

print(r.text,'\n************************************')

rqst.
