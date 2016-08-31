import requests

def Tile38_Command(command, IP=None , port=None ):
	'''
	This function acts like the tile38-cli executable binary 
	:param command: is a command that will be passed to the Tile38 server who will executed it , Check commands at: tile38.com/commands/
	:param type command is string

	:param IP: IP of the Tile38 , default here is localhost which is 127.0.0.1
	:param type IP is string

	:param port: port on which Tile38 is listening to ,default here is port 9851
	:param type port is unsigned int
	'''
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
	response = requests.post(url, data=data)
	return response.content	


#usage example
print Tile38_Command('get fleet abc1')
print '\n'
print Tile38_Command('set fleet abc12 point 13.4762 -111.10923','127.0.0.1')
print '\n'
print Tile38_Command('get fleet fb','127.0.0.1',9851)