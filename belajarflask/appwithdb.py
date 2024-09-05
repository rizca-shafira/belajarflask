from flask import render_template, Flask, request, redirect, url_for
import pymysql

app = Flask(__name__)

from transaction import transaction_bp
app.register_blueprint(transaction_bp)

from report import report_bp
app.register_blueprint(report_bp)

def connect_db():
    return pymysql.connect(
        host='localhost',
        user='sept',
        password='your_password',
        database='ayopy'
    )

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to get results as dictionaries
    cursor.execute("SELECT * FROM tbayoanggota")
    data = cursor.fetchall()  # Fetch all rows from the query result
    cursor.execute("SELECT * FROM tbayoadmin")
    dataadmin = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('form.html', data=data, dataadmin=dataadmin)
    #return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        #Tangkap data dari form
        name = request.form['name']
        email = request.form['email']
        action = request.form['action']
        role  = request.form['role']

        #Hubungkan ke db
        conn = connect_db()
        cursor = conn.cursor()

        #Masukkan data ke tabel user
        # query = "INSERT INTO tbayoanggota (nama_anggota, alamat) VALUES (%s, %s)"
        # cursor.execute(query, (name,email))
        # conn.commit()
        if role == 'Anggota':
            if action == 'Insert':
                # Insert data into the table
                query = "INSERT INTO tbayoanggota (nama_anggota, alamat) VALUES (%s, %s)"
                cursor.execute(query, (name, email))
                conn.commit()
            elif action == 'Update':
                # Update data in the table (you need to specify how to identify the record to update)
                query = "UPDATE tbayoanggota SET alamat = %s WHERE nama_anggota = %s"
                cursor.execute(query, (email, name))
                conn.commit()
            elif action == 'Delete':
                # Delete data from the table (you need to specify how to identify the record to delete)
                query = "DELETE FROM tbayoanggota WHERE nama_anggota = %s"
                cursor.execute(query, (name,))
                conn.commit()
        elif role == 'Admin':
            if action == 'Insert':
                # Insert data into the table
                query = "INSERT INTO tbayoadmin (nama_anggota, alamat) VALUES (%s, %s)"
                cursor.execute(query, (name, email))
                conn.commit()
            elif action == 'Update':
                # Update data in the table (you need to specify how to identify the record to update)
                query = "UPDATE tbayoadmin SET alamat = %s WHERE nama_anggota = %s"
                cursor.execute(query, (email, name))
                conn.commit()
            elif action == 'Delete':
                # Delete data from the table (you need to specify how to identify the record to delete)
                query = "DELETE FROM tbayoadmin WHERE nama_anggota = %s"
                cursor.execute(query, (name,))
                conn.commit()

        #Tutup koneksi
        cursor.close()
        conn.close()
    return redirect(url_for('index'))

@app.route('/updateadmin/<name>', methods=['GET', 'POST'])
def updateadmin(name):
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'POST':
        new_name = request.form['name']
        email = request.form['email']
        action = request.form['action']
        
        if action == 'Update':
            query = "UPDATE tbayoadmin SET nama_anggota = %s, alamat = %s WHERE nama_anggota = %s"
            cursor.execute(query, (new_name, email, name))
        elif action == 'Delete':
            query = "DELETE FROM tbayoadmin WHERE nama_anggota = %s"
            cursor.execute(query, (name,))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
    else:
        cursor.execute("SELECT * FROM tbayoadmin WHERE nama_anggota = %s", (name,))
        record = cursor.fetchone()
        cursor.close()
        conn.close()
        if record:
            return render_template('updatedeleteinput.html', record=record)
        else:
            return "Record not found", 404
        
@app.route('/deleteadmin', methods=['POST'])
def deleteadmin():
    name = request.form['name']
    
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM tbayoadmin WHERE nama_anggota = %s"
    cursor.execute(query, (name,))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/updateanggota/<name>', methods=['GET', 'POST'])
def updateanggota(name):
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'POST':
        new_name = request.form['name']
        email = request.form['email']
        action = request.form['action']
        
        if action == 'Update':
            query = "UPDATE tbayoanggota SET nama_anggota = %s, alamat = %s WHERE nama_anggota = %s"
            cursor.execute(query, (new_name, email, name))
        elif action == 'Delete':
            query = "DELETE FROM tbayoanggota WHERE nama_anggota = %s"
            cursor.execute(query, (name,))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
    else:
        cursor.execute("SELECT * FROM tbayoanggota WHERE nama_anggota = %s", (name,))
        record = cursor.fetchone()
        cursor.close()
        conn.close()
        if record:
            return render_template('updateanggota.html', record=record)
        else:
            return "Record not found", 404
        
@app.route('/deleteanggota', methods=['POST'])
def deleteanggota():
    name = request.form['name']
    
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM tbayoanggota WHERE nama_anggota = %s"
    cursor.execute(query, (name,))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)