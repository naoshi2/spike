from xml.etree.ElementTree import *

tree = parse("data.xml") 
elem = tree.getroot() 

print elem.tag
print elem.get("width")
print elem.get("height", "1200")
print elem.keys()
print elem.items()

# Modify value on width
elem.set("width", "1111")
print elem.get("width")

tree.write('output.xml')
