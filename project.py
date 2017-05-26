from flask import Flask, render_template, url_for, request, redirect
from collections import OrderedDict # import pour etre capable de generer un dictionnaire ordonne
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
    dict = OrderedDict() #declaration du dico pour quil soit ordonne
    categories = session.query(Category).order_by(Category.name)
    latestItems = session.query(Item).order_by(Item.id.desc()).all()
    for li in latestItems:
        id_of_item_category = li.category_id
        cate = session.query(Category).filter_by(id = id_of_item_category).one()
        dict[li] = cate
    return render_template('home.html', categories = categories, latestItems = latestItems, dict = dict)

# Show all Items for a Categorie
@app.route('/catalog/<string:elm>/items') #le fait de mettre <string:elm> permet de directement obtenir elm en string
def showItems(elm):
    element = session.query(Category).filter_by(name = elm).one()
    id = str(element.id)
    categories = session.query(Category).order_by(Category.name)
    output = ''
    items = session.query(Item).filter_by(category_id = id).all()
    #Pour retourner le nombre delement il ya dans cette query object
    nbr_items = session.query(Item).filter_by(category_id = id).count() 
    return render_template('categoryDescription.html', categories = categories, element = element, items = items, nbr_items = str(nbr_items))

# Show the description for one Item whatever the Categorie
@app.route('/catalog/<string:categorie>/<string:item>')
def showItemDescription(categorie, item):
    categories = session.query(Category).order_by(Category.name)
    cat = session.query(Category).filter_by(name = categorie).one()
    id = str(cat.id)
    item = session.query(Item).filter_by(category_id = id).filter_by(name = item).one() 
    return render_template('itemDescription.html',categories = categories, cat = cat, item = item)

@app.route('/catalog/<string:categorie>/<string:item>/Log')
def showItemDescriptionLog(categorie, item):
    categories = session.query(Category).order_by(Category.name)
    cat = session.query(Category).filter_by(name = categorie).one()
    id = str(cat.id)
    item = session.query(Item).filter_by(category_id = id).filter_by(name = item).one() 
    return render_template('itemDescriptionLog.html',categories = categories, cat = cat, item = item)

# Show the form for writing one Item an show its Categorie
@app.route('/catalog/<string:item>/edit', methods=['GET', 'POST'])
def showItemEdit(item):
    item = session.query(Item).filter_by(name = item).one()
    categories = session.query(Category).order_by(Category.name)
    category = session.query(Category).filter_by(id = item.category_id).one()
    #Ne pas essayer de definir la category de lelement a modifier car on fait un update et non un create
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']     
        session.add(item)
        session.commit()
        return redirect(url_for('showItems', elm = category.name))
    else:
        return render_template('itemEditionPage.html', item = item, categories = categories)

# Show the confirmation for deleting one Item an show its Categorie
@app.route('/catalog/<string:item>/delete', methods=['GET', 'POST'])
def showItemDelete(item):
    item = session.query(Item).filter_by(name = item).one()
    categories = session.query(Category).order_by(Category.name)
    category = session.query(Category).filter_by(id = item.category_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('showItems', elm = category.name))
    else:
        return render_template('itemDeletionPage.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
