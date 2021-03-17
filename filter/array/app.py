from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)
app.config['MONGODB_NAME'] = 'airbandb'
app.config['MONGO_URI'] = 'mongodb+srv://ubuntu:ubuntu@cluster0.aioov.mongodb.net/airbandb?retryWrites=true&w=majority'

#app.config['MONGODB_NAME'] = 'airbandb'
#app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/'
app.config['PROPAGATE_EXCEPTIONS'] = True
#cluster = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
# cluster = MongoClient("mongodb+srv://ubuntu:ubuntu@cluster0.aioov.mongodb.net/airbandb?retryWrites=true&w=majority")
# Database Name
#db = cluster["airbandb"]
# col = db["flat"]

mongo = PyMongo(app)



@app.route("/")
@app.route("/get_flats/", methods=["GET", "POST"])
def get_flats():
    flats = list(mongo.db.flat.find())
    return render_template('flats.html', flats=flats)

'''
        location = flat['host_location']
        description = flat['description']
        date = flat['last_scraped']
        print(flat['id': '28925'])
        return render_template('flats.html',
                               name=name,
                               location=location,
                               description=description,
                               date=date, )
'''
'''
    if request.method == "GET":
       get = {
            "location": request.form.get("host_location"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "date": request.form.get("last_scraped"),

        }
       mongo.db.tasks.find({"_id": ObjectId(id)}, get)
       flats = mongo.db.tasks.find_one({"_id": ObjectId(id)})
       location = mongo.db.location.find().sort("host_location", 1)
       return render_template("flats.html", name=flats, host_location=location)



@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    flats = list(mongo.db.flat.find({"$text": {"$search": query}}))
    return render_template("flats.html", name=flats)




'''

@app.route("/add_flat", methods=["GET", "POST"])
def add_flat():
    if request.method == "POST":
        flat = {
            "location": request.form.get("host_location"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "date": request.form.get("last_scraped"),

        }
        mongo.db.flats.insert_one(flat)
        flash("Flat Successfully Added")
        return redirect(url_for("/get_flats/"))

    locations = mongo.db.location.find().sort("host_location", 1)
    return render_template("add_flat.html", host_location=locations)

'''
@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))

'''

@app.route("/get_dates")
def get_dates():
    dates = list(mongo.db.categories.find().sort("last_scraped", 1))
    return render_template("get_dates.html", last_scraped=dates)

'''
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))

'''
if __name__ == '__main__':
    app.run(host='127.0.0.1')
    app.run(debug=True)
