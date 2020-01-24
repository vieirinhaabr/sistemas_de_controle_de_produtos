from flask import Flask, render_template
from API.DBConnector import DataBaseController

app = Flask(__name__)

dbconnector = DataBaseController()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    Products = dbconnector.get_products()

    if len(Products) > 0:
        return render_template('products.html', products = Products)
    else:
        msg = 'Nenhum produto encontrado'
        return render_template('products.html', msg = msg)

@app.route('/product/<string:id>/')
def product(id):
    Product = dbconnector.search_by_id(id)
    return render_template('product.html', product = Product[0])

if __name__ == '__main__':
    app.run(debug=True)
    