

class Countdown(object):
	def __init__(self,title,counter,interval):
		self.counter = counter
		self.title = title
		self.interval = interval
	def count(self):
		if self.counter == 0:
			reactor.callLater(1,globCounter)
		else:
			print self.title, self.counter, '...'
			self.counter -= 1
			reactor.callLater(self.interval, self.count)


from twisted.internet import reactor
mcounter = 3

def globCounter():
	global mcounter
	mcounter = mcounter -1
	if mcounter == 0:
		reactor.stop()
reactor.callWhenRunning(Countdown("First Counter: ",5,0.1).count)
reactor.callWhenRunning(Countdown("Second Counter: ",7,2).count)
reactor.callWhenRunning(Countdown("Third Counter: ",3,1.2).count)
print 'Start!'
reactor.run()
print 'Stop!'
