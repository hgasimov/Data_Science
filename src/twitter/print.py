'''
Created on May 31, 2013

@author: hgasimov
'''
import urllib
import json

url = "http://search.twitter.com/search.json?q=microsoft&page="
for i in range(1, 11):
    resp_json = urllib.urlopen(url + str(i))
    resp = json.load(resp_json)
    results = resp['results']
    for j in range(len(results)):
        print results[j]['text'].encode('utf-8')   
        