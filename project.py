from flask import Flask

app = Flask(__name__)

# Show all Catalog
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    return "Catalog page"

# Show all Items for a Categorie
@app.route('/catalog/<string:categorie>/items')
def showItems(categorie):
    return "Items Page"

# Show the description for one Item whatever the Categorie
@app.route('/catalog/<string:categorie>/<string:item>')
def showItemDescription(categorie, item):
    return "Item Description Page"

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
