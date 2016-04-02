import hashlib
import socket

def Calculate_hash_file(filename):
    h = hashlib.sha1()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


#apply encode method before passing to HashMessage. Addition can be done as Decide On type
def HashMessage(message):
    h=hashlib.sha1()
    h.update(message)
    return h.hexdigest()


class Server:
    'For Integrity of message HashMessage is Used, Hash of message is sent just after message usecases are corrpution check, providing large file on third party server, testing integrity of disk and images, file compare'
    def start(self):
        s=socket.socket()
        host =socket.gethostname()
        port =12345
        s.bind((host,port))

        s.listen(5)
        while True:
            c, addr = s.accept()
            print (' Got Connection from ', addr )
            message = 'Hello This is Message From Server'
            #send Message
            c.send(message.encode())
            #Send its hash
            c.send(HashMessage(message.encode()).encode())
            #below line is for wrong message
            #c.send(HashMessage((message+".").encode()).encode())
            c.close()


class Client:
    def start(self):
        s=socket.socket()
        host=socket.gethostname()
        port=12345

        s.connect((host,port))

        message = s.recv(1024)
        hash = s.recv(1024)

        print('Message at client = ',message)
        print('Hash at client = ',HashMessage(message))
        print('Hash received from server is = ',hash.decode())

        if HashMessage(message) == hash.decode() :
            print("Message received correctly ")

        else:
            print("Message is craafted")



        
#message = Calculate_hash_file("HashCalculator.py")
#print(message)

hash = HashMessage("Hello This Is Prashant".encode());
#print(hash)
