from BeautifulSoup import BeautifulSoup
import urllib
import bayes
import json
import sys


bor = bayes.BayesOnRedis(redis_host='localhost', redis_port=6379, redis_db=0)
#url = "http://www.amazon.com/Kindle-Fire-Amazon-Tablet/product-reviews/B0051VVOB2/ref=cm_cr_pr_hist_1?ie=UTF8&showViewpoints=0&filterBy=addTwoStar&pageNumber="
params = urllib.urlencode({'xhr': 1})
f = open("words-happy", 'a')
url = sys.argv[2] # e.g. "http://www.amazon.com/Kindle-Fire-Amazon-Tablet/product-reviews/B0051VVOB2/ref=cm_cr_pr_hist_1?ie=UTF8&showViewpoints=0&filterBy=addTwoStar&pageNumber="
category = sys.argv[1] # e.g. "sad"


for i in range(1,200):
	print
	print
	print url + str(i)
	print

	#import pdb; pdb.set_trace()
	if url.find("play.google") is not -1:
		dom = urllib.urlopen(url + str(i), params).read()
		json_reviews = json.loads(dom[5:])
		soup = BeautifulSoup(json_reviews['htmlContent'])
		reviews = soup.findAll('p')
		for review in reviews:
			try:
				text = review.getText()
				print "Feedback Length: " + str(len(text))
				bor.train(category, text)
				f.write(text)
				f.write("\n\n")
			except:
				pass
				
	elif url.find("amazon.com") is not -1:
		dom = urllib.urlopen(url + str(i)).read()
		soup = BeautifulSoup(dom)
		reviews = soup.findAll(id="productReviews")

		b = BeautifulSoup(str(reviews[0]))

		for x in range(23):
			if x % 3 == 0:
				try:
					text = b.findAll("div")[19].fetchNextSiblings()[x-1].getText()
					print "Feedback Length: " + str(len(text))
					bor.train(category, text)
					f.write(text)
					f.write("\n\n")
				except Exception, e:
					pass
