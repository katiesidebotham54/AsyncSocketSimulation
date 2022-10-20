import socket
import sys

port = int(sys.argv[1])
ts1_host = sys.argv[2]
ts1_port = sys.argv[3]
ts2_host = sys.argv[4]
ts2_port = sys.argv[5]


def main():

    # Create client socket to communicate with ts1
    try:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Client socket 1 for TS1 created")
    except socket.error as err:
        print("[S]: Couldn't create socket due to {}".format(err))
        exit()

    # Create client socket to communicate with ts2
    try:
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Client socket 2 for TS2 created")
    except socket.error as err:
        print("[S]: Couldn't create socket due to {}".format(err))
        exit()

    # Connect to TS1 host
    ts1_binding = (ts1_host, ts1_port)
    s1.connect(ts1_binding)

    # Connect to TS2 host
    ts2_binding = (ts2_host, ts2_port)
    s2.connect(ts2_binding)

    # Create socket to communicate with Client
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket for client created")
    except socket.error as err:
        print("[S]: Couldn't create socket due to {}".format(err))

    # Define the port on which you want to connect to the server
    hostname = socket.gethostname()
    localhost_addr = socket.gethostbyname(hostname)
    server_binding = (localhost_addr, port)
    ss.bind(server_binding)
    print("[S]: Successful Socket bind")
    ss.listen(1)

    # Accept connection from Client socket
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    while True:
        # Receive data from the client
        client_data = csockid.recv(200).decode('utf-8')
        if not client_data:
            break
        print("[C]: Data received from client: {}".format(
            client_data))
    ss.close()


if __name__ == "__main__":
    main()
    print("Done.")
