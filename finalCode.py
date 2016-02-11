import os
import zipfile
import xml.etree.ElementTree as ET

os.chdir("/Users/phanindra/Documents/open")

folders = []
files = []
Ids = []
types = []
names = []
versions = []
publicKeyTokens = []

z = zipfile.ZipFile(open("new.zip","rb"))

'''
for name in z.namelist():
    #z.extract(name)
    if(name[-1] == "/"):
        folders.append(name)
    else:
        print "file name : ",name
'''
z.extractall()

for tup in os.walk(os.getcwd()):
    print "***************************************\n"
    print "folder : ", tup[0]
    print "files in ",tup[0]
    filesList = tup[2]
    for i in range(len(filesList)):
                   print "file : ",filesList[i]
    print "\n"               


tree = ET.parse('parseme.xml')
for node in tree.iter():
    node.tag = node.tag.split("}")[1]
    if node.tag == 'supportedOS':
        if node.attrib.get("Id"):
            Ids.append(node.attrib.get("Id"))
    if(node.tag == "assemblyIdentity"):
        if node.attrib.get("type"):
            types.append(node.attrib.get("type"))
        if  node.attrib.get("name"):
            names.append(node.attrib.get("name"))
        if  node.attrib.get("version"):
            versions.append(node.attrib.get("version"))
        if node.attrib.get("publicKeyToken"):
            publicKeyTokens.append(node.attrib.get("publicKeyToken"))


print "Ids ", Ids
print "types ",types
print "names ",names
print "publicKeyTokens ",publicKeyTokens
print "versions ",versions
