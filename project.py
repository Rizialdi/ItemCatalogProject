from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item
 
engine = create_engine('sqlite:///categorymenu.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

# Show all Catalog
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).order_by(Category.name)
    output = ''
    for category in categories:
        output += category.name 
        output += '</br>'
    return output

# Show all Items for a Categorie
@app.route('/catalog/<string:elm>/items')
def showItems(elm):
    element = session.query(Category).filter_by(name = elm).one()
    id = str(element.id)
    output = ''
    items = session.query(Item).filter_by(category_id = id).all()
    output = ''
    for item in items:
        output += item.name 
        output += '</br>'
        output += item.description 
    return output

# Show the description for one Item whatever the Categorie
@app.route('/catalog/<string:categorie>/<string:item>')
def showItemDescription(categorie, item):
    cat = session.query(Category).filter_by(name = categorie).one()
    id = str(cat.id)
    output = ''
    item = session.query(Item).filter_by(category_id = id).filter_by(name = item).one() 
    output = ''
    output += item.description 
    return output

# Show the form for writing one Item an show its Categorie
@app.route('/catalog/<string:item>/edit')
def showItemEdit(item):
    return "Item Edition Page"

# Show the confirmation for deleting one Item an show its Categorie
@app.route('/catalog/<string:item>/delete')
def showItemDelete(item):
    return "Item Deletion Page"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
