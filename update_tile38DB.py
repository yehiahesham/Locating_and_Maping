import requests
import MySQLdb

class Tile38:
	#This function wrapps  tile38-cli executable
	def __init__(self,IP=None , port=None ):
		'''
			:param IP: IP of the Tile38 , default here is localhost which is 127.0.0.1
			:param type IP is string

			:param port: port on which Tile38 is listening to ,default here is port 9851
			:param type port is unsigned int
		'''
		if not IP:
			print "Default IP is assumed = localhost"
			self.IP='http://localhost'
		else:
		 self.IP='http://'+IP
		if not port:
			print "Default Port is assumed = 9851"
			self.port = 9851
		else:
			self.port = port
		self.url= str( self.IP)+":"+str(self.port)

	def Command(self,command, IP=None , port=None ):
		'''
		This function  acts like the tile38-cli sending commands to the  server
			:param command: is a command that will be passed to the Tile38 server who will executed it , Check commands at: tile38.com/commands/
			:param type command is string
		'''
		response = requests.post(self.url, data=command)
		return response.content





class DataBase:
	def __init__(self,connection,User,Password,Database):
		self.connection=connection
		self.User=User
		self.Password=Password
		self.Database=Database
		self.db = MySQLdb.connect(connection,User,Password,Database)

	def Insert(self,SQLStatment):
		cursor = self.db.cursor()
		try:
			cursor.execute(SQLStatment)
			db.commit()
		except:
			db.rollback()
		self.db.close()

	def Select(self,SQLStatment):
		cursor = self.db.cursor()
		cursor.execute(SQLStatment)
		results = cursor.fetchall()
		self.db.close()
		return results


#usage example

t= Tile38('127.0.0.1',9851)
db= DataBase('localhost','user','','BioMedical_DB')
c =  db.Select("SELECT ID, Name, Acc_Type, latitude, longitude FROM Accounts")
for row in c:
	name = row[1]
	lat=row[3]
	lng=row[4]
	print t.Command('set fleet '+str(name.replace(" ", "_"))+' point '+str(lat)+' '+str(lng))
print t.Command('nearby fleet point 33.462 -112.268 6000')
