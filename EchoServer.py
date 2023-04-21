import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maxBytesToReceive = 1024

serverIP = input("Enter IP address for server: ")
serverPort = input("Enter port number for server: ")

serverAddress = (serverIP, int(serverPort))

try:
    s.bind(serverAddress)
    s.listen(1)

    while True:
        print("Finding a connection...")
        sock, address = s.accept()

        try:
            while sock:
                res = sock.recv(maxBytesToReceive)
                msg = res.decode()
                if msg == "exit":
                    s.close() 
                    break 

                print("Message received: ", msg)
                print("Message all uppercase: ", msg.upper())
                sock.sendall(res.upper())            
        except:
            sock.close()
            s.close()
            print("Poor connection.")
        finally:
            sock.close()
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




