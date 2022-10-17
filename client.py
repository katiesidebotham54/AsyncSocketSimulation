import socket
import sys


def main():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    with open('RESOLVED.txt', 'w') as file:

        # close the client socket
    cs.close()
    exit()
