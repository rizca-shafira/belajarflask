from flask import Blueprint, render_template, request, redirect, url_for
import pymysql

transaction_bp = Blueprint('transaction', __name__)

def connect_db():
    return pymysql.connect(
        host='localhost',
        user='sept',
        password='your_password',
        database='ayopy'
    )

@transaction_bp.route('/transaction')
def transaction():
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    # Fetch data for dropdowns
    cursor.execute("SELECT nama_anggota FROM tbayoanggota")
    anggota_data = cursor.fetchall()
    
    cursor.execute("SELECT nama_anggota FROM tbayoadmin")
    admin_data = cursor.fetchall()

    cursor.execute("SELECT * FROM tbayotransaksi")
    transaksi_data = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return render_template('transaction.html', anggota_data=anggota_data, admin_data=admin_data, transaksi_data=transaksi_data)

@transaction_bp.route('/submit_transaction',methods=['POST'])
def submit_transaction():
    if request.method == 'POST':
        #Tangkap data dari form
        anggota = request.form['anggota']
        admin = request.form['admin']
        namabrg = request.form['namabrg']
        harga  = request.form['harga']
        qty = request.form['qty']

        #Hubungkan ke db
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # Fetch no_anggota from tbayoanggota
        cursor.execute("SELECT no_anggota FROM tbayoanggota WHERE nama_anggota = %s", (anggota,))
        no_anggota_row = cursor.fetchone()
        no_anggota = no_anggota_row['no_anggota'] if no_anggota_row else None

        # Fetch no_admin from tbayoadmin
        cursor.execute("SELECT no_anggota FROM tbayoadmin WHERE nama_anggota = %s", (admin,))
        no_admin_row = cursor.fetchone()
        no_admin = no_admin_row['no_anggota'] if no_admin_row else None

        # Check if the IDs were found
        if no_anggota is None or no_admin is None:
            # Handle error: missing IDs
            cursor.close()
            conn.close()
            return "Error: Invalid Anggota or Admin name", 400

        #Masukkan data ke tabel user
        query = "INSERT INTO tbayotransaksi (no_anggota, no_admin, nama_barang, harga, qty) VALUES (%s, %s,%s,%s,%s )"
        cursor.execute(query, (no_anggota,no_admin,namabrg,harga,qty))
        conn.commit()
        
        #Tutup koneksi
        cursor.close()
        conn.close()
    return redirect(url_for('transaction.transaction'))

@transaction_bp.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'POST':
        # Capture data from the form
        harga = request.form['harga']
        qty = request.form['qty']
        action = request.form.get('action')  # Ensure action is safely accessed
        
        if action == 'Update':
            query = "UPDATE tbayotransaksi SET harga = %s, qty = %s WHERE kode_transaksi = %s"
            cursor.execute(query, (harga, qty, name))
        elif action == 'Delete':
            query = "DELETE FROM tbayotransaksi WHERE kode_transaksi = %s"
            cursor.execute(query, (name,))
        
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('transaction.transaction'))
    
    else:
        cursor.execute("SELECT * FROM tbayotransaksi WHERE kode_transaksi = %s", (name,))
        record = cursor.fetchone()
        cursor.close()
        conn.close()
        if record:
            return render_template('updatetransaksi.html', record=record)
        else:
            return "Record not found", 404
        
@transaction_bp.route('/delete', methods=['POST'])
def delete():
    name = request.form['kode_transaksi']
    
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM tbayotransaksi WHERE kode_transaksi = %s"
    cursor.execute(query, (name,))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('transaction.transaction'))
