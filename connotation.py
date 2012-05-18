import bayes
import sqlite3

bor = bayes.BayesOnRedis(redis_host='localhost', redis_port=6379, redis_db=0)

#conn = sqlite3.connect("connotation.db")
#c = conn.cursor()

#for row in c.execute('''SELECT * FROM source_data'''):
	#print "Training..." + row[2]
	#bor.train(row[2], row[1])

#	print "Training...negative"
#	bor.train("sad", "sucks")

print bor.classify("love")
print bor.classify("bad bad dissapointed hate aweful sucks suck sucks sucks worst bad dissapointed sucks aweful terrible dissapointing crap dissapointed Very Dissapointed with Kindle Fire and Customer Service, you wont get the same tech twice! dissapointment total fail")
print bor.classify("You have some very real problems with your site. It's terrible and probably not secure.")
print bor.classify("this thing has some very serious problems which should be able to be fixed and some limitations")
print bor.classify("I love this!")
print bor.classify("This sucks!")
print bor.classify("I can't believe how terrible this site is!")
print bor.classify("blarg")







