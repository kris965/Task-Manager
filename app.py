import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
<<<<<<< HEAD
from bson.objectid import ObjectId 
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
=======
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = os.getenviron.get("MONGO_URI", "mongodb+srv://root:H00Gland7@myfirstcluster-1h0sc.mongodb.net/<kristianhoogland>?retryWrites=true&w=majority")
>>>>>>> cec1e9d69815109c02e6b87c64b6072a396714e7

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
<<<<<<< HEAD
    return render_template("tasks.html",
                           tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
=======
    return render_template("tasks.html", tasks=mongo.db.tasks.find())
>>>>>>> cec1e9d69815109c02e6b87c64b6072a396714e7


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
<<<<<<< HEAD
            debug=True)
=======
            debug=True)
>>>>>>> cec1e9d69815109c02e6b87c64b6072a396714e7
