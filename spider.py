from BeautifulSoup import BeautifulSoup
import urllib
import bayes
import json

bor = bayes.BayesOnRedis(redis_host='localhost', redis_port=6379, redis_db=0)
#url = "http://www.amazon.com/Kindle-Fire-Amazon-Tablet/product-reviews/B0051VVOB2/ref=cm_cr_pr_hist_1?ie=UTF8&showViewpoints=0&filterBy=addTwoStar&pageNumber="
params = urllib.urlencode({'xhr': 1})
url = "https://play.google.com/store/getreviews?id=com.google.android.street&reviewSortOrder=2&reviewType=1&rating=5&pageNum="
f = open("words-happy", 'a')

for i in range(1,200):
	print
	print
	print url + str(i)
	print
	#import pdb; pdb.set_trace()
	dom = urllib.urlopen(url + str(i), params).read()
	
	json_reviews = json.loads(dom[5:])
	soup = BeautifulSoup(json_reviews['htmlContent'])
	reviews = soup.findAll('p')
	for review in reviews:
		try:
			text = review.getText()
			print "Feedback Length: " + str(len(text))
			bor.train("happy", text)
			f.write(text)
			f.write("\n\n")
		except:
			pass
				