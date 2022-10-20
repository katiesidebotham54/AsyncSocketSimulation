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
        return DNS_table[hostname]
    except KeyError:
        return -1


def main():
    # Read mappings
    readFile()

    # Create TS socket
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[S]: TS1 Server socket created')
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    hostname = socket.gethostname()
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # Connect to the server on local machine
    port = int(sys.argv[1])
    server_binding = (localhost_addr, port)
    ss.bind(server_binding)
    ss.listen(1)

    # Accept a client
    csockid, addr = ss.accept()
    print()
    print("[S]: Got a connection, client is at {}".format(addr))


if __name__ == "__main__":
    main()
    print("Done.")
