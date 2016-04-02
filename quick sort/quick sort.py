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


def sort:
    return 0



parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = MovieHandler()
parser.setContentHandler( Handler )
   
parser.parse("test.xml")

print(str(Handler.outputlist))
