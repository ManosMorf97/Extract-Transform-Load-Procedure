from flask import Flask,render_template,url_for,request,redirect
from connection_to_mongodb import *

app = Flask(__name__)
full_name=""
db=get_database()
collection=db['Users_Products']

def getUsers():
    try:
        people=collection.find()
        return list(people)
    except Exception as ex:
        print(ex)
        return []

def getUserProducts(full_name):
    try:
        person=list(collection.find({'full_name':full_name}))[0]
        return person["products"]
    except Exception as ex:
        print(ex)
        return []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='GET':
        users=getUsers()
        return render_template('Search_User.html',users=users)
    else:
        full_name=request.form['search']
        return redirect(url_for('products',full_name=full_name))

@app.route('/user/<string:full_name>', methods=['GET', 'POST'])
def products(full_name):
    if request.method=='GET':
        products=getUserProducts(full_name)
        return render_template('Show_Products.html',products=products)
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
