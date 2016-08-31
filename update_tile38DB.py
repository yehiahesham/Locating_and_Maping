import requests

def Tile38_Command(command, IP=None , port=None ):
	data = command
	if not IP:
		print "Default IP is assumed = localhost"
		IP='http://localhost'
	else:
	 IP='http://'+IP
	if not port:
		print "Default Port is assumed = 9851"
		port = 9851
	url= str(IP)+":"+str(port)
	requests.post(url, data=data)

#usage example
Tile38_Command('set fleet abc1 point 12.4762 -111.10923')
print '\n'
Tile38_Command('set fleet abc2 point 13.4762 -111.10923','127.0.0.1')
print '\n'
Tile38_Command('set fleet abc3 point 14.4762 -111.10923','127.0.0.1',9851)
