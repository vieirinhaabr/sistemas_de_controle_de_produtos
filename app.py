from flask import Flask, render_template
from data import Products

app = Flask(__name__)

Products = Products()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html', products = Products)

@app.route('/product/<string:id>/')
def product(id):
    return render_template('product.html', id = id)

if __name__ == '__main__':
    app.run(debug=True)
    