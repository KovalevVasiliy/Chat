import socket, threading

def accept_client():
    while True:
        #accept
        cli_sock, cli_add = ser_sock.accept()
        uname = cli_sock.recv(1024).decode()
        CONNECTION_LIST.append((uname, cli_sock))
        print('%s connected' %uname)

def broadcast_usr():
    while True:
        for i in range(len(CONNECTION_LIST)):
            try:
                data = CONNECTION_LIST[i][1].recv(1024).decode()
                if data:
                    b_usr(CONNECTION_LIST[i][1], CONNECTION_LIST[i][0], data)
            except Exception as x:
                print(x.message)
                break

def b_usr(cs_sock, sen_name, msg):
    for i in range(len(CONNECTION_LIST)):
        if (CONNECTION_LIST[i][1] != cs_sock):
            CONNECTION_LIST[i][1].send(sen_name.encode())
            CONNECTION_LIST[i][1].send(msg.encode())

if __name__ == "__main__":
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5023
    ser_sock.bind((HOST, PORT))

    # listen
    ser_sock.listen(1)
    print('Chat started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()

    thread_bs = threading.Thread(target = broadcast_usr)
    thread_bs.start()