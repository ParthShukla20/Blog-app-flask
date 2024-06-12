from flask import Flask, render_template, request, redirect, session

import os
import psycopg2
from dotenv import load_dotenv


contact = '''CREATE TABLE IF NOT EXISTS contact (id SERIAL PRIMARY KEY, name  VARCHAR(40), email VARCHAR(40) , phone_number VARCHAR(20))'''

load_dotenv()
app = Flask(__name__)

url = os.getenv("DATABASE_URL")

connection = psycopg2.connect(url)

cur = connection.cursor()


query_insert = '''INSERT INTO contact (name,email,phone_number) VALUES  ('Parth', 'Parth@gmail.com','1234567890')'''

cur.execute(contact)
connection.commit()


@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET","POST"] )
def contact():
    if request.method == "POST":
        name=request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        query_insert = ("INSERT INTO contact (name, email, phone_number) VALUES (%s, %s, %s)")
        cur.execute(query_insert,(name,email,phone_number))
        connection.commit()
        cur.close()
        connection.close()
        return redirect("/contact")

    else:
        return render_template("contact.html")


if  __name__ == '__main__':
    app.run(port = 3000, debug=True)