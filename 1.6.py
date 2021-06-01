import xml.dom.minidom as minidom
import sys


class XmlStdin():
    def __init__(self):
        self.str = ""

    def write(self, value):
        self.str += value

    def toString(self):
        return self.str


dom = minidom.getDOMImplementation().createDocument(None, "root", None)
root = dom.documentElement
element = dom.createElement('test')
element.setAttribute('name', "i am student")
element.appendChild(dom.createTextNode("student"))
root.appendChild(element)
xmlStdin = XmlStdin()
sys.stdin = xmlStdin
dom.writexml(sys.stdin, addindent='\t', newl='\n', encoding='utf-8')
print(xmlStdin.toString())
