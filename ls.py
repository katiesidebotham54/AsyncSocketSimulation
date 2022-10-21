import socket
import sys
import select

# Command line arguments
port = int(sys.argv[1])
ts1_host = sys.argv[2]
ts1_port = int(sys.argv[3])
ts2_host = sys.argv[4]
ts2_port = int(sys.argv[5])


def main():
    # Create non-blocking load balancing server socket to communicate with client and servers
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: Load balancing server socket created")
    except socket.error as err:
        print("[LS]: Couldn't create socket due to {}".format(err))
        exit()

    # Define the port on which you want to connect to the LS server
    server_binding = ('', port)
    ls.bind(server_binding)
    ls.listen(1)

    # Accept connection from Client socket
    csockid, addr = ls.accept()
    print("[C]: Got a connection request from a client at {}".format(addr))

    # Create socket for communicating with TS1
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: TS1 socket created")
    except socket.error as err:
        print('[LS]: TS1 socket open error: {} \n'.format(err))
        exit()

    # Connect to the server TS1
    server_binding_ts1 = (ts1_host, ts1_port)
    ts1.connect(server_binding_ts1)

    # Create socket for communicating with TS2
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: TS2 socket created")
    except socket.error as err:
        print('[LS]: TS2 socket open error: {} \n'.format(err))
        exit()

    # Connect to the server TS2
    server_binding_ts2 = (ts2_host, ts2_port)
    ts2.connect(server_binding_ts2)

    while True:
        # Receive data from the client
        client_data = csockid.recv(200).decode('utf-8')
        if not client_data:
            break

        print("[C]: Data received from client: {}".format(
            client_data))

        # send a hostname query to the two servers directly
        ts1.send(client_data.encode('utf-8'))
        ts2.send(client_data.encode('utf-8'))

        # Use select to receive fastest response
        potential_readers = [ts1, ts2]
        potential_writers = []
        potential_errors = []

        ready_to_read, ready_to_write, in_error = \
                select.select(
                    potential_readers,
                    potential_writers,
                    potential_errors,
                    5)

        if len(ready_to_read) > 0:
            # receive IP address result from the server
            readable = ready_to_read[0]
            data_from_server = readable.recv(200).decode('utf-8')
            print("[TS]: Received result: {}".format(data_from_server))

            # send response back to client
            csockid.send(data_from_server.encode('utf-8'))
        else:
            # send error to client for no response
            error_msg = client_data + ' - TIMED OUT'
            csockid.send(error_msg.encode('utf-8'))

    ls.close()
    ts1.close()
    ts2.close()


if __name__ == "__main__":
    main()
    print("Done.")
