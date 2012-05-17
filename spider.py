from BeautifulSoup import BeautifulSoup
import urllib
import bayes

bor = bayes.BayesOnRedis(redis_host='localhost', redis_port=6379, redis_db=0)
url = "http://www.amazon.com/Kindle-Fire-Amazon-Tablet/product-reviews/B0051VVOB2/ref=cm_cr_pr_hist_1?ie=UTF8&showViewpoints=0&filterBy=addTwoStar&pageNumber="
f = open("words", 'a')

for i in range(1,117):
	print
	print
	print url + str(i)
	print
	dom = urllib.urlopen(url + str(i)).read()
	soup = BeautifulSoup(dom)
	reviews = soup.findAll(id="productReviews")

	b = BeautifulSoup(str(reviews[0]))

	for x in range(23):
		if x % 3 == 0:
			try:
				text = b.findAll("div")[19].fetchNextSiblings()[x-1].getText()
				print "Feedback Length: " + str(len(text))
				bor.train("sad", text)
				f.write(text)
				f.write("\n\n")
			except Exception, e:
				pass

			