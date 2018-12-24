from socket import *
import sys

# Ensure that user has entered a server port number argument when running .py script
try:
	n_port = int(sys.argv[1]) #Store port number from command line input
except IndexError:
	print("Please add server port number command line argument")

nportSocket = socket(AF_INET,SOCK_STREAM) # create TCP socket
nportSocket.bind(("",n_port)) # create bind socket to port number defined by n_port
nportSocket.listen(1) # listen for 1 connection


while True:
	connectionSocket, address = nportSocket.accept() #create new socket upon receiving incoming request.
	print("Connected to: " + address[0])
	while True:
		receivedCMD = connectionSocket.recv(1024).decode() #decode and store received command from client
		if (receivedCMD == "TOUPPERCASE" or receivedCMD == "TOLOWERCASE"):
			connectionSocket.send("OK")
		elif (receivedCMD == ""): #Occurs when client breaks connection and no cmd received
			print("Disconnected from: " + address[0])
			connectionSocket.close()
			break
		else:
			print("Improper input commands received")
		client_address = connectionSocket.recv(1024).decode() #decode and store received client addr
		r_port = int(connectionSocket.recv(1024).decode()) #decode and store received client port number
		print("Received the client address: " + client_address)
		print("Received the client port: " + str(r_port))
		transactionSocket = socket(AF_INET,SOCK_STREAM) #create transaction TCP socket
		transactionSocket.connect((client_address,r_port)) #connect from server to client
		msg = transactionSocket.recv(1024).decode() #retrieve msg from client 
		if (receivedCMD == "TOUPPERCASE"):
			transactionSocket.send(msg.upper().encode())
		elif (receivedCMD == "TOLOWERCASE"):
			transactionSocket.send(msg.lower().encode())
		else:
			print("No recognized command received")
		
		