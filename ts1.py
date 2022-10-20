import socket
import sys

# Mappings
DNS_table = {}

# Mapping Value Indices
ORG_HOSTNAME = 0
IP_ADDRESS = 1
RECORD_TYPE = 2


def readFile():
    file = open("PROJ2-DNSTS1.txt", "r")
    Lines = file.readlines()

    # adding values to DNS_table
    for line in Lines:
        query = line.strip()
        split_query = query.split(' ')

        org_hostname = split_query[0]
        key_hostname = split_query[0].lower()
        ip_address = split_query[1]
        record_type = 'A'

        DNS_table[key_hostname] = org_hostname, ip_address, record_type

    file.close()


def host_lookup(hostname):
    try:
        return DNS_table[hostname.lower()]
    except KeyError:
        return -1


def create_response(query_value):
    response = '{} {} {} IN'.format(query_value[ORG_HOSTNAME],
                                    query_value[IP_ADDRESS,
                                    query_value[RECORD_TYPE]])


def main():
    # Read mappings
    readFile()

    # Create TS socket
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[S1]: TS1 Server socket created')
    except socket.error as err:
        print('[S1] ERROR - Socket open error: {}\n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = int(sys.argv[1]) # as entered in command line
    server_binding = ('', port)
    ss.bind(server_binding)
    ss.listen(1)

    # Accept a client
    host = socket.gethostname()
    print("[S1]: TS1 Server host name is {}".format(host))
    localhost_ip = socket.gethostbyname(host)
    print("[S1]: TS1 Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print("[LS]: Got a connection request from a client at {}".format(addr))

    # Receive data from the client
    while True:
        client_query = csockid.recv(200).decode('utf-8')
        if not client_query:
            break
        
        print("[LS]: Data received from load server: {}".format(
            client_query))
        
        # Host lookup
        host_value = host_lookup(client_query)

        # Send value if exists
        if not host_value == -1:
            response = create_response(host_value)
            csockid.send(reversed_msg.encode('utf-8'))


if __name__ == "__main__":
    main()
    print("Done.")
