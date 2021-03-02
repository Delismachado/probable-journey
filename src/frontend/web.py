from flask import Flask, render_template, request, redirect

from src.controllers.category_controller import CategoryController
from src.models.category import Category

app = Flask(__name__)

controller = CategoryController()


@app.route('/')
def categories():
    list_categories = controller.read_all()
    return render_template('category.html', categories=list_categories)


@app.route('/category_create')
def category_create_form():
    id_resul = request.args.get('id')
    if id_resul:
        category = controller.read_by_id(int(id_resul))
        return render_template('category_create.html', update=True, category=category)
    return render_template('category_create.html')


@app.route('/category_create', methods=['POST'])
def category_create():
    name = request.form.get('name')
    description = request.form.get('description')
    new_category = Category(name, description)
    controller.create(new_category)
    return redirect('/')


@app.route('/category_update', methods=['POST'])
def category_update():
    id_resul = int(request.form.get('id'))
    name = request.form.get('name')
    description = request.form.get('description')
    category = controller.read_by_id(id_resul)
    category.name = name
    category.description = description
    controller.update(category)
    return redirect('/')


@app.route('/category_delete')
def category_delete():
    id_resul = int(request.args.get('id'))
    category = controller.read_by_id(id_resul)
    controller.delete(category)
    return redirect('/')


app.run(debug=True)
