from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item
 
engine = create_engine('sqlite:///categorymenu.db')
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


#Item for Soccer
category1 = Category(name = "Soccer")

session.add(category1)
session.commit()


item1 = Item(name = "Football", description = "Essential element for a good match", category = category1)

session.add(item1)
session.commit()

item2 = Item(name = "Whistle", description = "To avoid bad practice, it's essential for a referee", category= category1)

session.add(item2)
session.commit()


#Item for Basketball
category2 = Category(name = "Basketball")

session.add(category2)
session.commit()


item1 = Item(name = "Ball", description = "Essential element for a good match", category = category2)

session.add(item1)
session.commit()

item2 = Item(name = "Jordan", description = "Yes, its true, if you wanna play like him, take this shoe", category= category2)

session.add(item2)
session.commit()


#Item for Roller
category3 = Category(name = "Roller")

session.add(category3)
session.commit()


item1 = Item(name = "Pair of Roller", description = "Essential element bro, think about it", category = category3)

session.add(item1)
session.commit()

item2 = Item(name = "Wheel", description = "Dont worry, you dont need to by a new shoe, we have the solution", category= category3)

session.add(item2)
session.commit()

#Item for Snowboarding
category4 = Category(name = "Snowboarding")

session.add(category4)
session.commit()


item1 = Item(name = "Goggles", description = "Yes bro, you only have two eyes", category = category4)

session.add(item1)
session.commit()

item2 = Item(name = "Snowboard", description = "I dont really know why, we everyone take also it", category= category4)

session.add(item2)
session.commit()

print("added items!")

