import socket

# Creates a new socket object. Utilizes the AF_INET address family and the SOCK_STREAM socket type. 
# Therefore, it will be using the IPv4 addresses and the TCP protocol for sending/receiving data.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# maximum number of bytes to receive from the server in a single recv().
maxByteToReceive = 1024


# User inputs ip, port, and msg
print("Client\n")
serverAddress = input("Type in the server's IP address: ")
serverPort = input("Type in the server's port number: ")
msg = input("Type in the message that you want to send to the server: ")

# Runs forever until the client is closed or encounters an error. 
# In the loop, it connects to the server using the IP address and port number that was given by the user.
while True:
    try:
        print("Attempting to connect to ", serverAddress, ", Port: ", serverPort, "\n")
        s.connect((serverAddress, int(serverPort)))
        # If successful, user can keep sending message to the server and waits for a response. 
        # this continues until the user types "exit".
        print("Connection Successful!\n")

        while msg != "exit":
            print("Sending msg to server!\n")
            s.sendall(msg.encode())

            res = s.recv(maxByteToReceive)
            print("Response from server: ", res.decode(), "\n")
            msg = input("Type in the message that you want to send to the server: ")
        
        # When the user types "exit", the server closes as well as the client 
        msg = "exit"
        s.sendall(msg.encode())
        res = s.recv(maxByteToReceive)
        print("Response from server: ", res.decode(), "\n")
        print("Closing client....")
        
    except socket.timeout:
        print("Connection timed out!")
    except socket.gaierror:
        print("Invalid IP address. Try again.")
    except ValueError:
        print("Invalid port number. Try again.")
    finally:
        break
s.close()