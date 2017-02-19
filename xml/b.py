from xml.etree.ElementTree import *

tree = parse("data2.xml") 
root = tree.getroot() 

for child in root:
    print child.tag, child.attrib

    # year
    #print child[1].text

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank


for rank in root.iter('rank'):
    rank.text = 'void'


tree.write('output2.xml')
