from twisted.internet import reactor
from twisted.internet.task import LoopingCall

class Countdown(object):
	counter = 5

	def count(self):
		if self.counter == 0:
			lc.stop()
		else:
			print self.counter, '...'
			self.counter -= 1
			reactor.callLater(1, self.count)

			
lc = LoopingCall(Countdown().count)

print "Start!"
lc.start(0.1)


reactor.run()
print "Stop!"