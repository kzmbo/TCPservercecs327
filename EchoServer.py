import socket

# Creates a new socket object. Utilizes the AF_INET address family and the SOCK_STREAM socket type. 
# Therefore, it will be using the IPv4 addresses and the TCP protocol for sending/receiving data.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# maximum number of bytes to receive from the server in a single recv().
maxBytesToReceive = 1024

# User inputs the server's ip and port number
serverIP = input("Enter IP address for server: ")
serverPort = input("Enter port number for server: ")

# creates server address with given ip and port number
serverAddress = (serverIP, int(serverPort))

# attempts to bind the address and listen
try:
    s.bind(serverAddress)
    s.listen(1)

    # if a connection is found, take the msg and make all of the letter uppercase
    while True:
        print("Finding a connection...")
        sock, address = s.accept()

        try:
            isRunning = True
            while isRunning:
                res = sock.recv(maxBytesToReceive)
                msg = res.decode()

                print("Message received: ", msg)
                print("Message all uppercase: ", msg.upper())
                sock.sendall(res.upper())

                if msg == "exit":
                    isRunning = False
                    print("Closing server...")
                    sock.close()              
        except:
            sock.close()
            s.close()
            print("Poor connection.")
        finally:
            s.close()
            break
except ValueError:
    print("Incorrect port number")
except socket.timeout:
    print("Connection timed out!")
except socket.gaierror:
    print("Invalid IP address. Try again.")     
finally:
    s.close()




