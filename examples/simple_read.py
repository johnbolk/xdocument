"""simple_read.py - Create and read a simple XML document."""

from xdocument import XDocument

document = XDocument('Simple.xml', 'Root', 'A Simple XML Document')
if document.root.first_child is None:
    child = document.root.add('Child', 'Attrib', 'Value')
    child.add('GrandChild').value = 'Text'
    document.save()
# -----------------------------------------------------------------
else:  # Read and print the contents of the XML document
    child = document.root.first_child
    print(f"Attribute Value = {child.read_attribute('Attrib')}")
    print(f"GrandChild Value = {child.read_child('GrandChild')}")
