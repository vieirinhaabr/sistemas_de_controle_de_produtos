from flask import Flask, render_template, flash, redirect, url_for, request
from API.DBConnector import DataBaseController
from wtforms import Form, StringField, TextAreaField, validators

app = Flask(__name__)

dbconnector = DataBaseController()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products', methods=['GET', 'POST'])
def products():
    form = SearchForm(request.form)
    Products = dbconnector.get_products()

    if request.method == 'POST' and form.validate():
        search = form.search.data

        result = dbconnector.search_by_name(search)

        return render_template('products.html',  products = result, form = form)

    if len(Products) > 0:
        return render_template('products.html', products = Products, form = form)
    else:
        msg = 'Nenhum produto encontrado'
        return render_template('products.html', msg = msg, form = form)

@app.route('/product/<string:id>/')
def product(id):
    Product = dbconnector.search_by_id(id)
    return render_template('product.html', product = Product[0])

class ProductForm(Form):
    name = StringField('Nome')
    description = TextAreaField('Descrição')
    price = TextAreaField('Preço')
    amount = TextAreaField('Quantidade')

class SearchForm(Form):
    search = StringField('Pesquisar Produtos')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        description = form.description.data
        price = form.price.data
        amount = form.amount.data

        dbconnector.create(name, description, price, amount)

        flash('Produto salvo', 'success')

        return redirect(url_for('products'))

    return render_template('add_product.html', form = form)

@app.route('/edit_product/<string:id>', methods=['GET', 'POST'])
def edit_article(id):
    Product = dbconnector.search_by_id(id)
    Product = Product[0]

    form = ProductForm(request.form)
    form.name.data = Product[1]
    form.description.data = Product[2]
    form.price.data = Product[3]
    form.amount.data = Product[4]

    if request.method == 'POST' and form.validate():
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        amount = request.form['amount']

        dbconnector.update(Product[0], name, description, price, amount)

        flash('Produto atualizado', 'success')

        return redirect(url_for('products'))

    return render_template('edit_product.html', form=form)

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'redsfsfsfsfis'
    app.run(debug=True)
    