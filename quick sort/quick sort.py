import xml.sax
import threading

class XMLHandler( xml.sax.ContentHandler ):
    'Class for parsing xml. All rules fr parsing are defined in this class'
    def __init__(self):
        self.CurrentData = ""
        self.outputlist=list()

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'Number':
            print ("*****Number*****")

    def endElement(self, tag):
        if tag == 'Number':
            print ("Number:", self.Number)
            self.outputlist.append(int(self.Number))
     
    def characters(self, content):
        if self.CurrentData == "Number":
            self.Number = content

class myThread(threading.Thread):
    'This class creates new thread each time. Thread calls quicksort function '
    def __init__(self,sort,i,j):
        threading.Thread.__init__(self)
        self.sort_object=sort
        self.i = i
        self.j = j
    def run(self):
        #print("thread started - ",str(self.i),str(self.j))
        self.sort_object.quicksort(self.i,self.j)

class sorting:
    'Sorting functionality, it uses above class for parallelism.'
    def __init__(self,input):
        self.input_list = input
        self.length = len(input)
        self.quicksort(0,self.length-1)
    def partition(self,i,j):
        pivot_place=i
        pivot = self.input_list[i]
        print(str(i),' ' ,str(j))
        while i<j:
            while pivot >= self.input_list[i] and i <j:
                i+=1
            while pivot < self.input_list[j]:
                j-=1
            if(i<j):
                self.input_list[i],self.input_list[j]=self.input_list[j],self.input_list[i]
        self.input_list[pivot_place],self.input_list[j] = self.input_list[j], self.input_list[pivot_place]
        print(str(self.input_list))
        return j;
    
    def quicksort(self,i,j):
        m=0
        if(i<j):
            m = self.partition(i,j)
            t1=myThread(self,i,m-1)
            t2=myThread(self,m+1,j)
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        return 0

    

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = XMLHandler()
parser.setContentHandler( Handler )
   
parser.parse("test.xml")

print(str(Handler.outputlist))
s= sorting(Handler.outputlist)
print(str(s.input_list))
