from socket import *
import sys

try:
	serverName = sys.argv[1] #Take server address from 1st cmd line argument
except IndexError:
	print("Missing command line input parameters")

try:
	serverPort = int(sys.argv[2]) #Take server port number from 2nd cmd line argument
except IndexError:
	print("Missing server address or port number parameters")

clientSocket = socket(AF_INET, SOCK_STREAM) #create TCP socket on client 
clientSocket.connect((serverName,serverPort)) #attempt to connect to server based on given serverName and port number

#Keep prompting user for proper input command 
while True:
	command = raw_input("Enter either 'TOUPPERCASE' or 'TOLOWERCASE' commands or 'EXIT' to exit: ")
	if (command.strip().upper() in ["TOUPPERCASE", "TOLOWERCASE"]):
		clientSocket.send(command.strip().upper().encode()) #Send input command to server
		serverResponse = clientSocket.recv(1024).decode() #Receive ok response
		if (serverResponse == "OK"):
			serverSocket = socket(AF_INET, SOCK_STREAM) #Create a server socket on client
			serverSocket.bind(("", 0)) #Select a free port for binding
			serverSocket.listen(1) #Listen for 1 connection from socket
			print("The following free port has been selected: " + str(serverSocket.getsockname()[1]))
			clientSocket.send(clientSocket.getsockname()[0].encode()) #Send client address to server
			clientSocket.send(str(serverSocket.getsockname()[1]).encode()) #Send client port number to server as a string
			transactionSocket, address = serverSocket.accept() #create transaction socket when receiving server request
			while True: #handle case where no input msg is provided (user only hits enter)
				msg = raw_input("Input message to be converted: ") #User inputs string to be modified
				if (msg == ""):
					print("No message was entered. Please enter a message...")
				else:
					break
			transactionSocket.send(msg.encode()) #string is sent to server
			modifiedMsg = transactionSocket.recv(1024).decode() #receive modified string from server
			print("Here is the modified message: " + modifiedMsg)
			serverSocket.close() #Close data connection
		else:
			print("Server OK response not received")
	elif (command.strip() in ["EXIT", "exit"]):
		clientSocket.close() #Close persistent connection to server
		break
	else:
		print("You have entered: " + "'" + command + "'" + ". The only accepted commands are 'TOUPPERCASE' and 'TOLOWERCASE'")

