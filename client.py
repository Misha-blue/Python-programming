import socket
import operator

import time


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
        except:
            raise ClientError()

    def put(self, metric, value, timestamp=int(time.time())):
        request = "put {} {} {}\n".format(metric, value, timestamp)
        self.sock.sendall(request.encode("utf8"))
        reply = self.sock.recv(1024)
        if reply == b'ok\n\n':
            return
        else:
            raise ClientError()

    def get(self, key):
        request = "get {}\n".format(key)
        self.sock.sendall(request.encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")
        return self.to_dict(data)

    @staticmethod
    def to_dict(string):
        data = {}
        string = string.strip("ok").split()
        for i in range(0, len(string), 3):
            try:
                timestamp = int(string[i + 2])
                metric = float(string[i + 1])
                if string[i] in data.keys():
                    data[string[i]].append((timestamp, metric))
                else:
                    data[string[i]] = [(timestamp, metric)]
            except:
                raise ClientError()
        for key in data.keys():
            data[key].sort(key=operator.itemgetter(0))
        return data


class ClientError(Exception):
    pass
