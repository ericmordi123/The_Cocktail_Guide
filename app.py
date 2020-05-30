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
                           

@app.route('/recipe')
def recipe():
    return render_template("recipe.html", recipe=mongo.db.recipe.find(), alcohols=mongo.db.alcohols.find())

@app.route('/addrecipe')
def addrecipe():
    return render_template("addrecipe.html", alcohols=mongo.db.alcohols.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = {
            'cocktail': request.form.get('cocktail'),
            'alcohol': request.form.get('alcohol'),
            'difficulty': request.form.get('difficulty'),
            'description': request.form.get('description'),
            'ingredients': request.form.getlist('add_ingredient[]'),
            'instructions_step_1': request.form.get('instructions_step_1'),
            'instructions_step_2': request.form.get('instructions_step_2'),
            'instructions_step_3': request.form.get('instructions_step_3'),
            'alcohol_rating': request.form.get('alcohol_rating'),
            'cocktail_image': request.form.get('cocktail_image'),
            'prep_time': request.form.getlist('prep_time')
            }
    recipes = mongo.db.recipe
    recipes.insert_one(recipe)
    return redirect(url_for('recipe'))

@app.route('/cocktail_recipe/<recipe_id>')
def cocktail_recipe(recipe_id):
    the_cocktail_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cocktails = mongo.db.alcohols.find()
    return render_template('cocktailrecipe.html', recipe=the_cocktail_recipe, alcohols=all_cocktails)

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('recipe'))

@app.route('/edit_recipe/<recipe_id>')
def editrecipe(recipe_id):
    cocktail_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cocktails = mongo.db.alcohols.find()
    return render_template('editrecipe.html', recipe=cocktail_recipe, alcohols=all_cocktails)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipe
    recipes.update( {"_id": ObjectId(recipe_id)},
    {
            'cocktail': request.form.get('cocktail'),
            'alcohol': request.form.get('alcohol'),
            'difficulty': request.form.get('difficulty'),
            'description': request.form.get('description'),
            'ingredients': request.form.getlist('ingredients'),
            'instructions_step_1': request.form.get('instructions_step_1'),
            'instructions_step_2': request.form.get('instructions_step_2'),
            'instructions_step_3': request.form.get('instructions_step_3'),
            'alcohol_rating': request.form.get('alcohol_rating'),
            'cocktail_image': request.form.get('cocktail_image'),
            'prep_time': request.form.getlist('prep_time')
    })
    return redirect(url_for('recipe'))

@app.route('/add_cocktail', methods=['POST'])
def add_cocktail():
    alcohol = {
            'cocktail': request.form.get('cocktail'),
    }
    alcohols = mongo.db.alcohols
    alcohols.insert_one(alcohol)
    return redirect(url_for('recipe'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT',5000)),
            debug=True)