'''
Created on May 31, 2013

@author: hgasimov
'''
import urllib
import json

resp_json = urllib.urlopen("http://search.twitter.com/search.json?q=Microsoft")
resp = json.load(resp_json)
results = resp['results']
for i in range(len(results)):
    print results[i]['text'].encode('utf-8')