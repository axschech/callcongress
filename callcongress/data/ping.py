import requests
from xml.etree import ElementTree

class Senators():
  url = 'https://www.senate.gov/general/contact_information/senators_cfm.xml'
 
  def get(self):
    r = requests.get(self.url, headers={'user-agent': 'my-app/0.0.1'});
#     print r.content
    tree = ElementTree.fromstring(r.content)
    objects = []
    for x in tree:
      object = {}
      for z in x:
        object[z.tag] = z.text
      objects.append(object)
    return objects
  
senators = Senators()
print len(senators.get())