import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'the_cocktail_guide'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-ldgtk.mongodb.net/the_cocktail_guide?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipe=mongo.db.recipe.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)