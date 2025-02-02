import socket
import tkinter as tk
import time


def transmit_file(destination_address, file_name):
    # Function to transmit the file. Contains the code copy/pasted from phase1
    # Takes as input the host address to send the file to and the name for the file upon arrival

    # Initialization of the socket object and connects it to the port and host address
    client_socket = socket.socket()
    port = 8090
    client_socket.connect((destination_address, port))

    # Open file in read-binary mode
    file_to_send = open(file_name, 'rb')

    # Find the length of the file, calculate the number of packets, and print all info
    file_to_send.seek(0, 2)
    file_length = file_to_send.tell()
    num_of_packets = int(file_length / 1024) + 1
    file_to_send.seek(0, 0)
    print(file_length)
    print(file_name)
    print(num_of_packets)

    # Encode the file name and num_of_packets and send them to the server
    encoded_file_name = file_name.encode()
    client_socket.send(encoded_file_name)
    time.sleep(1)  # Delay by 1 second
    string_num_of_packets = str(num_of_packets)
    encoded_string_num_of_packets = string_num_of_packets.encode()
    client_socket.send(encoded_string_num_of_packets)

    # Loop to keep sending packets and print the packet number that is being sent
    for x in range(1, num_of_packets + 1):
        num_of_packets_send_string = f"Sending packet #{x} to the server..."
        print(num_of_packets_send_string)
        data = file_to_send.read(1024)
        client_socket.send(data)
    file_to_send.close()

    # Display that the data has been sent successfully
    print("\nData has been sent successfully!")

    return


def close_program(event):
    # Closes the program
    window.quit()
    return


def send_file(event):
    # Event to send the file once the user has clicked the "Send file" button
    destination_address = ent_destination.get()
    file_name = ent_file_name.get()
    print(file_name)

    # Close the window and send the file
    window.destroy()
    transmit_file(destination_address, file_name)

    # Display the confirmation the file sent
    lbl_file_sent = tk.Label(text="The file has been sent.")
    lbl_file_sent.pack()

    btn_confirm_exit = tk.Button(text="Click to exit.", width=16, height=2)
    btn_confirm_exit.pack()
    btn_confirm_exit.bind('<Button-1>', close_program)

    return


# Get the name of this machine to use as a default address
default_server_name = socket.gethostname()
window = tk.Tk()

# Introductory message
lbl_introduction = tk.Label(text="UDP transferring files")
lbl_introduction.pack()

# Get the destination name from the user, default to default_server_name
ent_destination = tk.Entry()
ent_destination.pack()
ent_destination.insert(0, default_server_name)

# Get the file name from the user. Default to sample.jpg
lbl_get_file_name = tk.Label(text="\n Enter the file name: ")
ent_file_name = tk.Entry()
lbl_get_file_name.pack()
ent_file_name.pack()
ent_file_name.insert(0, "flowerblue.jpg")

btn_confirm_entry = tk.Button(text="Transmit File", height=2, width=10)
btn_confirm_entry.pack()
btn_confirm_entry.bind('<Button-1>', send_file)

window.mainloop()
