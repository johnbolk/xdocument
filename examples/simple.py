"""simple.py - Create a simple XML document."""

from xdocument import XDocument

document = XDocument('Simple.xml', 'Root', 'A Simple XML Document')
if document.root.first_child is None:
    child = document.root.add('Child', 'Attrib', 'Value')
    child.add('GrandChild').value = 'Text'
    document.save()
