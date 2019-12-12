import socket,time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((host, port))

quit = False
print("[ Server started ]")
print("["+ host +"]")

while not quit:
    try:
        data, addr = sock.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        print("[" + addr[0] + "] = [" + str(addr[1]) +"] = [" + itsatime + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                sock.sendto(data, client)
    except:
        print("\n[ Server stopped ]")
        quit = True
sock.close()