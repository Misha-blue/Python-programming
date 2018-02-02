import asyncio
import operator
from collections import OrderedDict

store_dict = OrderedDict()


def run_server(host, port):
    def process_data(data):
        error_wrong_command = "error\nwrong command\n\n"
        ok = "ok\n"
        end = "\n"

        if data.startswith("get"):
            try:
                command, key = data.split()
                if key in store_dict.keys():
                    store_dict[key].sort(key=operator.itemgetter(1))
                    values = store_dict[key]
                    message = ""
                    if values is not None:
                        for i in range(len(values)):
                            message += key + " " + " ".join(values[i]) + '\n'
                    return ok + message + end
                elif key == "*":
                    message = ""
                    for key in store_dict.keys():
                        store_dict[key].sort(key=operator.itemgetter(1))
                        values = store_dict[key]
                        if values is not None:
                            for i in range(len(values)):
                                message += key + " " + " ".join(values[i]) + '\n'
                    return ok + message + end
                else:
                    return ok + end
            except ValueError:
                return error_wrong_command
        elif data.startswith("put"):
            try:
                command, key, timestamp, metric = data.split()
                if key in store_dict.keys() and (timestamp, metric) not in store_dict[key]:
                    store_dict[key].extend([(timestamp, metric)])
                elif key not in store_dict.keys():
                    store_dict[key] = [(timestamp, metric)]
                return ok + end
            except ValueError:
                return error_wrong_command
        else:
            return error_wrong_command

    class ClientServerProtocol(asyncio.Protocol):

        def connection_made(self, transport):
            self.transport = transport

        def data_received(self, data):
            resp = process_data(data.decode())
            self.transport.write(resp.encode("utf-8"))

    loop = asyncio.get_event_loop()

    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()