from flask import Flask, render_template, url_for, request, redirect, session as sess
#when importing session as sess we must set the secret_key on the application to something unique and secret
from collections import OrderedDict # import pour etre capable de generer un dictionnaire ordonne
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
import os
 
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


################################################################################################################


@app.route('/login', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username is None or password is None:
            error_message = "missing arguments"
            return render_template('signin.html', error_message =  error_message)
            
        if session.query(User).filter_by(username = username).first() is not None:
            error_message = "existing user"
            return render_template('signin.html', error_message =  error_message) #in these error cases return blank form
            
        user = User(username = username)
        user.hash_password(password)
        session.add(user)
        session.commit()
        #in this case redirect the newly created user to sign up page
        return redirect(url_for('signup_user', usrname = username))
    else:
        return render_template('signin.html')  #in this case return only a blank form

@app.route('/logout', methods=['GET', 'POST'])
def logout_user():
    sess['logged_in'] = False
    return render_template('logout.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #by using <required> in <input> <tag>, we can remove this part
        if username is None or password is None:
            error_message =  "missing arguments"
            return render_template('signup.html', error_message = error_message)  #in this case return only a blank form

        user_object = session.query(User).filter_by(username = username).first() 
        if user_object is not None and user_object.verify_password(password):
            sess['logged_in'] = True
            return redirect(url_for('showCatalog'))
        else:
            error_message = "User/Pwd not find in database... Try again or go to Login Page"
            return render_template('signup.html', error_message = error_message)
    else:
        return render_template('signup.html', usrname = request.args.get('usrname'))  #in this case return only a blank form

@app.route('/user')
def user():
    user = session.query(User).all()
    output = ''
    for u in user:
        output += u.username
        output += '</br>'
        output += u.password_hash
        output += '</br>'
    return output

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
