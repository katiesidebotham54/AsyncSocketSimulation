import socket
import sys

# Command line arguments
port = int(sys.argv[1])
ts1_host = sys.argv[2]
ts1_port = int(sys.argv[3])
ts2_host = sys.argv[4]
ts2_port = int(sys.argv[5])


def main():

    # Create load balancing socket to communicate with client and servers
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: Client socket 1 for TS1 created")
    except socket.error as err:
        print("[LS]: Couldn't create socket due to {}".format(err))
        exit()

    # Define the port on which you want to connect to the server
    server_binding = ('', port)
    ls.bind(server_binding)
    ls.listen(1)

    # Accept connection from Client socket
    csockid, addr = ls.accept()
    print("[C]: Got a connection request from a client at {}".format(addr))

    while True:
        # Receive data from the client
        client_data = csockid.recv(200).decode('utf-8')
        if not client_data:
            break

        print("[C]: Data received from client: {}".format(
            client_data))

        try:
            sent = ls.send(client_data)
            total_sent += sent
            client_data = client_data[sent:]
            print('Sending data')
        except e:
            if e.errno != errno.EAGAIN:
                print('Blocking with', len(data), 'remaining')
                select.select([], [ss], [])  # This blocks until
        
        response = -1

        # Send value if exists
        if not response == -1:
            csockid.send(response.encode('utf-8'))
        else:
            error_msg = client_data + ' - TIMED OUT'
            csockid.send(error_msg.encode('utf-8'))

    ss.close()


if __name__ == "__main__":
    main()
    print("Done.")
