from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("orders.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return "OK"


@app.route("/products")
def products():

    products_list = [
        {"name": "Laptop", "price": 60000},
        {"name": "Keyboard", "price": 2000},
        {"name": "Mouse", "price": 1000}
    ]

    return render_template(
        "products.html",
        products=products_list
    )


@app.route("/orders")
def orders():

    connection = get_db_connection()

    orders_list = connection.execute(
        "SELECT * FROM orders"
    ).fetchall()

    connection.close()

    return render_template(
        "orders.html",
        orders=orders_list
    )

@app.route("/dashboard")
def dashboard():

    connection = get_db_connection()

    total_orders = connection.execute(
        "SELECT COUNT(*) FROM orders"
    ).fetchone()[0]

    total_revenue = connection.execute(
        "SELECT COALESCE(SUM(price), 0) FROM orders"
    ).fetchone()[0]

    pending_orders = connection.execute(
        "SELECT COUNT(*) FROM orders WHERE status = 'Pending'"
    ).fetchone()[0]

    connection.close()

    return render_template(
        "dashboard.html",
        total_orders=total_orders,
        total_revenue=total_revenue,
        pending_orders=pending_orders
    )


@app.route("/add-order", methods=["POST"])
def add_order():

    product_name = request.form["product_name"]
    price = request.form["price"]

    connection = get_db_connection()

    connection.execute(
        "INSERT INTO orders (product_name, price, status) VALUES (?, ?, ?)",
        (product_name, price, "Pending")
    )

    connection.commit()
    connection.close()

    return redirect("/orders")


if __name__ == "__main__":
    app.run(debug=True)