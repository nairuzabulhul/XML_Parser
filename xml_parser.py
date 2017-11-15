
import csv
import requests
import xml.etree.ElementTree as ET



def parseXML(xmlfile):

    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create text file

    parsedFile = open('parsedXML.txt','a')
    
    output =[]

    for i in  root.findall('./'):

        output.append(i.attrib)

        
    
    for vals in output :

        for one_item in vals:


           parsedFile.write(one_item +": " + vals[one_item].encode("utf-8"))
           parsedFile.write("\n\n")
        parsedFile.write("\n")
        parsedFile.write("-----------------------------------------------------------------------\n")
          
             
    parsedFile.close()     
           
          
         

parseXML('Major Incident List Report XML.xml')
  
