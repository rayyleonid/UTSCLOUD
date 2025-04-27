from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Koneksi ke database RDS
conn = mysql.connector.connect(
    host="bajudb.cncqac8okmlo.ap-southeast-2.rds.amazonaws.com",  # Ganti dengan endpoint RDS yang sesuai
    user="admin",  # Ganti dengan username RDS
    password="rayyanleonid11",  # Ganti dengan password RDS
    database="baju"  # Ganti dengan nama database yang sesuai
)

cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM produk;")
    rows = cursor.fetchall()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
