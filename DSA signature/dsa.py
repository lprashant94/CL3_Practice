import Hashlib

message ='Hello there'
p=5

q=10
g=4

r=0
s=0



def HashMessage(message):
    h=hashlib.sha1()
    h.update(message)
    return h.hexdigest()






print(str(r))
print(str(s))
