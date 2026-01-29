import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://18.207.94.13:8000/")

print("Addition:", server.add(10, 5))
print("Subtraction:", server.subtract(10, 5))
