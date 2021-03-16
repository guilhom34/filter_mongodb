from flask import Flask, render_template, request, redirect, url_for, logging
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
# Database Name
db = client["filter"]
col = db["tableau"]
tabs = col.find_one()

def data():
    tabs = col.find()
    return tabs
    print(tabs)

@app.route("/")
def home():
    data = data()
    for tab in data:
        name = "tab.name";
        url = "tab.listing_url";
        date = "tab.last_scraped";
    return render_template('index.html', members=db.find())

'''
@app.route("/create")
def create(ref, new_tag ):
    db.create({'ref': ref}, {'$push': {'tags': new_tag}})
    return render_template('create.html')


@app.route("/save", methods=['POST'])
def save():
    name = request.form['name']
    relation = request.form['relation']
    phone = request.form['phone']
    email = request.form['email']

    data = {"name": name, "relation": relation, "phone": phone, "email": email}

    db.insert_one(data)
    return redirect(url_for('home'))


@app.route("/edit/<string:id>")
def edit(id):
    result = db.find_one({"_id": ObjectId(id)})
    return render_template('edit.html', room=result)


@app.route("/update", methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    relation = request.form['relation']
    phone = request.form['phone']
    email = request.form['email']

    data = {"name": name, "relation": relation, "phone": phone, "email": email}

    db.update_one({'_id': ObjectId(id)}, {"$set": data}, upsert=False)
    return redirect(url_for('home'))


@app.route("/delete/<string:id>", methods=['GET', 'DELETE'])
def delete(id):
    if request.method == 'DELETE':
        if request.json:
            params = request.json
        else:
            params = request.form

        id = params.get('id')

    db.remove({"_id": ObjectId(id)})
    return redirect(url_for('home'))

'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

