from socket import *

#创建tcp套接字
s = socket()
s.bind(("0.0.0.0",8998))
s.listen(5)

while True:
    c,addr = s.accept()
    print("Connect from ",addr)
    data = c.recv(4096)
    print(data)

    #返回http响应
    data = """HTTP/1.1 200 OK
 
    Content-Type: text/html

    <h1>Welcome to tedu</h1>
    <p>Python test</p>
    """

    c.send(data.encode())
    c.close()

s.close()
