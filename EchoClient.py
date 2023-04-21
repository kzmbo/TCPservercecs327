import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Client\n")
serverAddress = input("Type in the server's IP address: ")
serverPort = input("Type in the server's port number: ")
msg = input("Type in the message that you want to send to the server: ")

while True:
    try:
        print("Attempting to connect to ", serverAddress, ", Port: ", serverPort, "\n")
        s.connect((serverAddress, int(serverPort)))
        print("Connection Successful!\n")

        print("Sending msg to server!\n")
        s.sendall(msg.encode())

        res = s.recv(1024)
        print("Response from server: ", res.decode(), "\n")
        while True:
            msg = input("Type in the message that you want to send to the server: ")
            
            print("Sending msg to server!\n")
            s.sendall(msg.encode())

            res = s.recv(1024)
            print("Response from server: ", res.decode(), "\n")
            if msg == "exit":
                s.close()
                break

    except socket.timeout:
        print("Connection timed out!")
    except socket.gaierror:
        print("Invalid IP address. Try again.")
    except ValueError:
        print("Invalid port number. Try again.")
    finally:
        s.close()
        break