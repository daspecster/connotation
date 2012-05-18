import urllib
from BeautifulSoup import BeautifulSoup
import bayes
import sys

bor = bayes.BayesOnRedis(redis_host='localhost', redis_port=6379, redis_db=0)

#url = "http://news.ycombinator.com/threads?id=" + sys.argv[1]
url = "http://news.ycombinator.com/item?id=" + sys.argv[1]

dom = urllib.urlopen(url).read()
soup = BeautifulSoup(dom)
comments = soup.findAll("span", {"class": "comment"})

happies = 0
sads = 0

for comment in comments:
	text = comment.getText()
	connotation = bor.classify(text)# + " - " + text
	if connotation == "sad":
		sads = sads + 1
	elif connotation == "happy":
		happies = happies + 1
	else:
		print "Unknown"


print "Happies: " + str(happies)
print
print "Sads: " + str(sads)

print
print "Happiness score... > 7 is happy: " + str(happies / sads)
if (happies / sads) > 7:
	print "This article is happy!"
elif happies == sads:
	print "This article is neutral."
else:
	print "This article is sad :("