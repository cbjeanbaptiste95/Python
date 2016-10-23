from socket import *

lskt = socket(AF_INET, SOCK_STREAM)
lskt.bind(('localhost',1400))

## listens for a connection
lskt.listen(SOMAXCONN)

print "listening"

while True:
	cskt, client_address = lskt.accept()
	print str(client_address)

	## wait to recieve message/data
	msg = cskt.recv(2048)
	print "message: " + str(msg)

	cskt.sendall(msg)
	## redirect message to sender
	lskt.sendall(str(msg))

cskt.close()

##  this might be the right way of doing it
## http://stackoverflow.com/questions/9852045/how-to-make-a-simple-proxy-in-python
## http://voorloopnul.com/blog/a-python-proxy-in-less-than-100-lines-of-code/
## http://www.binarytides.com/python-socket-server-code-example/
## http://stackoverflow.com/questions/9852045/how-to-make-a-simple-proxy-in-python
