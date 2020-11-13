#!/usr/bin/python3
import socket, select, string, sys, threading
 
HOST = "178.62.94.90"
PORT = 5000

USER_INPUT_READY = False
USER_INPUT_STRING = ""

SERVER_MESSAGE_READY = False
SERVER_MESSAGE_STRING = ""
 
def prompt() :
	sys.stdout.write('<You> ')
	sys.stdout.flush()

def spawnServerListener(sock):
	t = threading.Thread(target=getServerMessage, args=(sock,), daemon=True)
	t.start()

def spawnUserListener():
	t = threading.Thread(target=getUserInput, daemon=True)
	t.start()
	 
def getServerMessage(sock):
	global SERVER_MESSAGE_READY
	global SERVER_MESSAGE_STRING
	binary_message = sock.recv(4096)
	if binary_message:
		msg = binary_message.decode("UTF-8")
		SERVER_MESSAGE_READY = True
		SERVER_MESSAGE_STRING = msg

def getUserInput():
	global USER_INPUT_READY
	global USER_INPUT_STRING
	msg = sys.stdin.readline()
	USER_INPUT_READY = True
	USER_INPUT_STRING = msg

#main function
if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print("Attempting to connect to server...")
		sock.connect((HOST, PORT))
	except:
		print('Unable to connect')
		sys.exit()

	print("Connected to remote host. Press enter to send a message. Type '/exit' or '/quit' to leave.")
	welcome_msg = sock.recv(2048).decode("UTF-8")
	print("\n" + welcome_msg)
	prompt()
	spawnServerListener(sock)
	spawnUserListener()
	while True:
		if SERVER_MESSAGE_READY:
			SERVER_MESSAGE_READY = False
			sys.stdout.write(SERVER_MESSAGE_STRING)
			prompt()
			spawnServerListener(sock)
		elif USER_INPUT_READY:
			USER_INPUT_READY = False
			if USER_INPUT_STRING[0] == '/':
				args = USER_INPUT_STRING[1:].split(' ', 1)
				command = args[0].rstrip()
				if command == 'exit' or command == 'quit':
					sock.close()
					sys.exit()

			sock.send(bytes(USER_INPUT_STRING, "UTF-8"))
			prompt()
			spawnUserListener()
