import socket
import sys

port = int(sys.argv[1])
ts1_host = sys.argv[2]
ts1_port = sys.argv[3]
ts2_host = sys.argv[4]
ts2_port = sys.argv[5]


def main():
    try:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Client socket for TS1 created")
    except socket.error as err:
        print("[S]: Couldn't create socket due to {}".format(err))
        exit()

    # create client socket to communicate with ts2
    try:
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Client socket 2 for TS2 created")
    except socket.error as err:
        print('socket 2 open error: {} \n'.format(err))
        exit()

    # Connect to TS1 host
    s_address1 = (ts1_host, ts1_port)
    s1.connect(s_address1)

    # Connect to TS2 host
    s_address2 = (ts2_host, ts2_port)
    s2.connect(s_address2)


if __name__ == "__main__":
    main()
    print("Done.")
