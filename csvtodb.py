from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Area
 
engine = create_engine('sqlite:///subzonedata.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Adding all zones to db
for line in open("subzones_ggn.csv"):
	csv_row = line.split(",")
	print csv_row
	area1 = Area(subzone_id=int(csv_row[0]),subzone_name=csv_row[1],latitude=float(csv_row[2]),longitude=float(csv_row[3])
	print area1
	session.add(area1)
	session.commit()

print "added menu items!"
