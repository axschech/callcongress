import requests
from xml.etree import ElementTree
from callcongress.db import person

class Senators():
  url = 'https://www.senate.gov/general/contact_information/senators_cfm.xml'
 
  def get(self):
    person.drop_tables()
    r = requests.get(self.url, headers={'user-agent': 'my-app/0.0.1'});

    tree = ElementTree.fromstring(r.content)
    objects = []
    for x in tree:
      try:
        first = x[1].text
        last = x[2].text
        party = x[3].text
        state = x[4].text
        phone = x[6].text
        email = x[7].text
        try:
          with person.db_session:
            person.Person(first_name=first, last_name=last, party=party, state=state, phone=phone, email=email)
        except Exception, e:
          print str(e)
      except:
        print "failed assign"

senators = Senators()
senators.get()