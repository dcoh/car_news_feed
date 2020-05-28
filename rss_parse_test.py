import csv
import unicodedata
import json
import urllib2

#Testing how to use the rss2json REST API call to parse RSS feeds into JSON and print out data
inputTestFile = open('feed_list.txt')
inputTestArray = []
rssToJsonUrl = "https://api.rss2json.com/v1/api.json?rss_url="
for line in inputTestFile:
    inputTestArray.append(line)

for item in inputTestArray:
    fileString = item.split(",")
    for url in fileString:
        rssToJsonUrl = "https://api.rss2json.com/v1/api.json?rss_url="
        url = rssToJsonUrl+url
        response = urllib2.urlopen(url)
        data = json.loads(response.read());

        #print url
        for item in data['items']:
            print item['title']
