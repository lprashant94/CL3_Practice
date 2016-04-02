import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
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

class sorting:
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
            self.quicksort(i,m-1)
            self.quicksort(m+1,j)

        
        return 0



parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = MovieHandler()
parser.setContentHandler( Handler )
   
parser.parse("test.xml")

print(str(Handler.outputlist))
s= sorting(Handler.outputlist)
print(str(s.input_list))
