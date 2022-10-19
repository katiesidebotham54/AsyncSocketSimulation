import socket
import sys

# Queries array
queries = []


def read_queries():
    file = open("PROJ2-HNS.txt", "r")
    Lines = file.readlines()

    # adding values to DNS_table
    for query in Lines:
        queries.append(query.strip().lower())


if __name__=='__main__':
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Defining the port to connect to the load balancing server
    localhost_addr = sys.argv[1]
    port = sys.argv[2]

    # connect to the server
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # process and store queries
    with open('RESOLVED.txt', 'w') as file:
        for query in queries:
            # send a hostname query to the server
            cs.send(query.encode('utf-8'))

            # receive IP address result from the server
            data_from_server=cs.recv(200).decode('utf-8')
            print("[C]: Received result: {}".format(data_from_server))

            # store result
            file.write(data_from_server + '\n')

    # close the client socket
    cs.close()
    exit()
