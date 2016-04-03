import math,random,hashlib

class DSA:
    def __init__(self,p,q,g):
        self.p=p
        self.q=q
        self.g=g
        self.x=0
        self.y=0
        
    def Signature(self,message):
        r=0
        s=0
        #this loop can go infinite if p,q,g and x,y are very small
        #can prevent this loop by generating new key pair if it fails more that expected.
        while s==0:
            while r==0:
                k = int(random.random()*(self.q-1))+1
                r = (self.g**k)%self.p%self.q
            a1= (int(self.HashMessage(message.encode()),16)+self.x *r) % self.q
            print('k is ',str(k),str(self.q-2))
            a2 = (k ** (self.q-2)) % self.q
            s=int(a1*a2)%self.q
        
            
        print(str((r,s)))
        self.verify(message,r,s)
        return (r,s)
    
    def verify(self,messsage,r,s):
        print('Verifying')
        if r==0 or s==0:
            return False
        #special code line for finding w*s= 1 mod q where s and q are known
        w= (s**(self.q-2))%self.q
        u1 = int(self.HashMessage(message.encode()),16)*w
        u1=u1%self.q
        u2= (r*w)%self.q
        v= (((self.g**u1)*(self.y**u2))%self.p)%self.q
        print(str((v,r,w,s,self.q)))
        if v==r:
            print("Signature validated")
            return True
        else:
            print("Wrong signature")
            return False

    def HashMessage(self,message):
        h=hashlib.sha1()
        h.update(message)
        return h.hexdigest()

    def GenerateKeyPair(self):
        print('Private and public key pair is -')
        while self.x == 0 or self.y ==0:
            self.x =int(random.random()*(self.q-1))+1
            self.y = (self.g**self.x)%self.p
        print(str(self.x))
        print(str(self.y))

message ='Hello there'
d=DSA(7,3,4)
d.GenerateKeyPair()
r,s = d.Signature(message)
print('r ,s pair is ',str(r),str(s))
d.verify(message,r,s)

d= DSA(23,11,4)
d.GenerateKeyPair()
r,s = d.Signature(message)
print('r ,s pair is ',str(r),str(s))
d.verify(message,r,s)

d= DSA(1279,71,1157)
d.GenerateKeyPair()
r,s = d.Signature(message)
print('r ,s pair is ',str(r),str(s))
d.verify(message,r,s)

d= DSA(797,199,81)
d.GenerateKeyPair()
r,s = d.Signature(message)
print('r ,s pair is ',str(r),str(s))
d.verify(message,r,s)

