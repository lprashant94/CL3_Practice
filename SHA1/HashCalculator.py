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


class SHA1:
    def __init__(self):
        self.h0 = int('01100111010001010010001100000001',2)
        self.h1 = int('11101111110011011010101110001001',2)
        self.h2 = int('10011000101110101101110011111110',2)
        self.h3 = int('00010000001100100101010001110110',2)
        self.h4 = int('11000011110100101110000111110000',2)
        print(str(hex(self.h0)))
        print(str(hex(self.h1)))
        print(str(hex(self.h2)))
        print(str(hex(self.h3)))
        print(str(hex(self.h4)))
        
    def HashMessage(self,message):
        print(message,len(message));
        return 1


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

a=SHA1()
a.HashMessage("Hello This Is Prashant".encode())


hash = HashMessage("Hello This Is Prashant".encode());
#print(hash)
