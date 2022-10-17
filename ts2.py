import socket
import sys

DNS_table = {}


def readFile():
    file = open("PROJ2-DNSTS2.txt", "r")
    Lines = file.readlines()

    # adding values to table
    for line in Lines:
        query = line.strip()
        split_query = query.split(' ')
        hostname = split_query[0].lower()
        ip_address = split_query[1]
        DNS_table[hostname] = ip_address

    file.close()


def is_host_in_DNS_table(hostname):
    if hostname in DNS_table.keys():
        return True
    else:
        return False


def main():
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
