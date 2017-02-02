from pony.orm import *

sql_debug(True)

db = Database();

class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    email = Required(str)
    phone = Required(str)
    party = Required(str)
    state = Required(str)

def drop_tables():
  db.drop_all_tables(with_all_data=True)
  db.create_tables()
  
db.bind('sqlite', 'db.db', create_db=True)
db.generate_mapping(create_tables=True)