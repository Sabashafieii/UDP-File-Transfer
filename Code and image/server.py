import socket

server_socket = socket.socket()  # Renamed socketVar to server_socket
host_name = socket.gethostname()
port = 8090
server_socket.bind((host_name, port))
server_socket.listen(1)  # Wait for 1 incoming connection

print(host_name)

while True:
    print("Waiting for connection...")
    connection, address = server_socket.accept()

    print(address, "has connected to the server")

    # Receives the file name and number of packets from the client
    file_name = connection.recv(1024)
    file_name = file_name.decode()
    num_of_packets = connection.recv(1024)
    decoded_num_of_packets = num_of_packets.decode()
    num_of_packets = int(decoded_num_of_packets)

    # Open the file in write-binary mode
    file = open(file_name, 'wb')

    # Loops to keep receiving packets and prints the packets being received from the client
    for x in range(1, num_of_packets + 1):
        num_of_packets_recv_string = f"Receiving packet #{x} from client..."
        print(num_of_packets_recv_string)
        data = connection.recv(1024)
        file.write(data)
    connection.close()
    file.close()

    print("\nData has been transmitted successfully!\n")



