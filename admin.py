import mysql.connector
from flask import Flask, render_template, request, redirect

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_123",
    database="gs"
)

# Define a Flask app
app = Flask(__name__)

# Route to display the data from the add_place table
@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM add_place")
    data1 = cursor.fetchall()
    cursor.execute("SELECT * FROM add_item")
    data2 = cursor.fetchall()
    return render_template('admin.html', data1=data1, data2=data2)

# Route to handle the approval of place data
@app.route('/approvePlace')
def approvePlace():
    cursor = db.cursor()
    name = request.args.get('name')

    # Fetch the data from the add_place table
    cursor.execute("SELECT * FROM add_place WHERE id=%s", (name,))
    data = cursor.fetchone()

    # Insert the data into the place table
    cursor.execute("INSERT INTO place (p_name, p_description) VALUES (%s, %s)",(data[1], data[2]))
    
    # Delete the data from the add_place table
    cursor.execute("DELETE FROM add_place WHERE id=%s", (name,))
    db.commit()
    # return 'Data approved'
    return redirect('/')

# Route to handle the approval of item data
@app.route('/approveItem')
def approveItem():
    cursor = db.cursor()
    name = request.args.get('name')

    # Fetch the data from the add_place table
    cursor.execute("SELECT * FROM add_item WHERE id=%s", (name,))
    data = cursor.fetchone()

    # Insert the data into the place table
    cursor.execute("INSERT INTO item (location, i_name, i_description) VALUES (%s, %s, %s)",(data[1], data[2],data[3]))
    
    # Delete the data from the add_place table
    cursor.execute("DELETE FROM add_item WHERE id=%s", (name,))
    db.commit()
    # return 'Data approved'
    return redirect('/')

if __name__ == '__main__':
    app.run()