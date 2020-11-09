import xml.sax
from starting_coroutine_using_decorator import start_coroutine

class EventHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target
    def startElement(self, name, attrs):
        self.target.send(('start', (name, attrs._attrs)))
    def characters(self, text):
        self.target.send(('text', text))
    def endElement(self, name):
        self.target.send(('end', name))

if __name__ == '__main__':
    @start_coroutine
    def printer():
        while True:
            event = (yield)
            print("Printer is printing", event)

    xml.sax.parse("allroutes.xml", EventHandler(printer()))