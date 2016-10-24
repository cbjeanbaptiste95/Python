from socket import *
from threading import *

def handle_client(cskt):
    request = cskt.recv(2048)

    print request

    req = request.split()
    print req
    # Split req[1] along the slashes
    print ("next execution starts here ")
    drop_slashs = req[1].split('/')
    print drop_slashs

    # Create socket to connect to the "real" website (as a client)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect('', 1400)
    # Send GET request to the "real" web server.
    data = s.recv(2048)
    s_split = s.split()
    msg = s_split[4]
    # Read the reply. Say reply is placed in msg


    cskt.sendall(msg)

    cskt.close()

    


lskt = socket(AF_INET, SOCK_STREAM)
lskt.bind( ('', 1400) )

lskt.listen(SOMAXCONN)
print SOMAXCONN

while True:
    cskt, cli_addr = lskt.accept()
    t = Thread(target = handle_client, args=(cskt,))
    t.start()
