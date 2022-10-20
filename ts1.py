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

# Search DNS Table for specific hostname and return corresponding tuple if exists
# Format: DomainName IPaddress A IN


def host_lookup(hostname):
    try:
        msg = str(DNS_table[hostname][ORG_HOSTNAME]) + " " + str(
            DNS_table[hostname][IP_ADDRESS]) + " " + str(DNS_table[hostname][RECORD_TYPE])
        return msg
    except KeyError:
        return -1


def main():
    # Read mappings
    readFile()

    # Create TS socket for communicating with LS
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[S]: TS1 Server socket created')
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    hostname = socket.gethostname()
    localhost_addr = socket.gethostbyname(hostname)

    # Connect to the server on local machine
    port = int(sys.argv[1])
    server_binding = (localhost_addr, port)
    ss.bind(server_binding)
    ss.listen(1)

    # Accept a client
    csockid, addr = ss.accept()
    print("[S]: Got a connection, client is at {}".format(addr))


if __name__ == "__main__":
    main()
    print("Done.")
