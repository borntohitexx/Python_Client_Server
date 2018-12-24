# Python TCP Client & Server

Completed TCP client & server in Python for school assignment. 
Client sends uppercase or lowercase command to the server.
Server will then translate any incoming messages from the client into uppercase or lower case defined earlier.

## Getting Started
Ensure that Python is installed on computer

## Instructions
In terminal/command line run the following command to start server.py first.
Server.py takes in one argument: Port Number
This tells the server which port should be open to listen for incoming TCP connections from client 
Ideally, use any port number from 1024 to 65535 to avoid using restricted ports

Run the server as "python server.py [port number]"

Example:

```
python server.py 34000 
```

Make note of the port number that the server has been started on. You will need to tell the client to connect to the server using this port number

Next you will need to open a new terminal session and start client.py
Client.py accepts two arguments:
  1. Server address (locally would be 127.0.0.1)
  2. Server port number (same number as the one used to start the server on)

Example:

 ```
 python client.py 127.0.0.1 34000
 ```
 
 User should then be prompted to either enter a 'TOUPPERCASE' or 'TOLOWERCASE' or 'EXIT' command
 The 'TOUPPERCASE' command will tell the server to modify anything you send next into uppercase.
 The 'TOLOWERCASE' command will tell the server to modify anything you send next into lowercase.
 
 Example:
 
 ```
 "Enter either 'TOUPPERCASE' or 'TOLOWERCASE' commands or 'EXIT' to exit: "
 >> TOUPPERCASE
 ```
 
 The user will be prompted to enter a message to be translated
 
 Example: 
 
 ```
 "Input message to be converted: "
 >> Hello World
 ```
 
 The server will then return the modified message to the client to be printed 
 
 ```
 >> HELLO WORLD
 ```
 
 ## Test Cases
 
 1. Server should not stop even when client has been closed. A new client can be re-started and connected to server 
 2. Client should not send any commands to the server that is not either "TOUPPERCASE" or "TOLOWERCASE". This includes CTRL+C shortcut.
 
 **This program was tested on the Linux servers provided by the Computer Science Computing Facility at University of Waterloo**
