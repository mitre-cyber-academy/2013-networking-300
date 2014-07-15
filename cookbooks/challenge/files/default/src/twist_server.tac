from twisted.internet import protocol, reactor
from twisted.application import internet, service

#Riddles to give the order of the sequences
udpMessages = {
	49: 'I sound like the past verb of gluttony. It is for this reason that my predecessor is feared and my successor is `gone.\' I am the first cube.', #Ate/8
	52: 'I am the first prime after a sequence of three which are not.' #11
}

tcpMessages = {
	77: 'I am unity. Conjoined, united, together. The primal anthem.', #1
	67: 'I am symmetry. Yin and yang. Paired forces orbiting. Duality.', #2
	65: 'The energy of creation unleashed; my name is where the world split for the first time.', #Trinity -> 3
	45: 'Golfers will say my name, although with a different meaning. I am the first square.', #Fore -> 2 ** 2 -> 4
	53: 'I am the number of points for the first star. I am odd and prime.', #5
	52: 'When tripled, I am thought to be evil. I sound like a command to an attack dog.', #666/'Sic' -> 6
	49: 'When tripled, I am thought to be lucky. My squared self is one less than twice a quarter.', #777/50 - 1 = 49 = 7 ** 2 -> 7
	66: 'I sound like a negative in another language. I am the second square', #Nein -> 9
	48: 'All your base are belong to me. Except those of the programmers and the mathemeticians...', #Base 10 (vs 2, 8, 16, etc.) -> 10
	55: 'I am the product of the second prime and the first square.', #3 * 4 -> 12
}

class RiddleProtocolT(protocol.Protocol):
	def connectionMade(self):
		#Get the given port:
		port = self.transport.getHost().port
		#Get the message:
		message = tcpMessages.get(port, 'Enigma am I') + '\r\n'
		#Write out the riddle
		self.transport.write(message)
		self.transport.loseConnection()


class RiddleFactoryT(protocol.ServerFactory):
	protocol = RiddleProtocolT

class RiddleProtocolU(protocol.DatagramProtocol):

	def __init__(self, localPort):
		self.port = localPort
	def datagramReceived(self, data, (host, port)):
		self.transport.write(
			udpMessages.get(self.port, 'Enigma am I')
			+ '\r\n', (host, port))
		

application = service.Application('riddle', uid=1, gid=1)
for port in tcpMessages.keys():
	internet.TCPServer(port, RiddleFactoryT()).setServiceParent(
			service.IServiceCollection(application))

for port in udpMessages.keys():
	internet.UDPServer(port, RiddleProtocolU(port)).setServiceParent(
			service.IServiceCollection(application))
