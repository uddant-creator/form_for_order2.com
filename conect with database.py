from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="UddantS4213.m",
    database="ssp"
)
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        product_name VARCHAR(100),
        city VARCHAR(100),
        state VARCHAR(100),
        address TEXT,
        phone VARCHAR(20),
        date DATE
    )
""")
db.commit()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        product_name = request.form['product_name']
        city = request.form['city']
        state = request.form['state']
        address = request.form['address']
        phone = request.form['phone']
        date = request.form['date']  # New field

        sql = """
            INSERT INTO orders (name, product_name, city, state, address, phone, date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, product_name, city, state, address, phone, date)
        cursor.execute(sql, values)
        db.commit()

        return "Form submitted successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
