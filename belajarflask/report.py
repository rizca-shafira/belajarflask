from flask import Blueprint, render_template, request, redirect, url_for
import pymysql

report_bp = Blueprint('report', __name__)

def connect_db():
    return pymysql.connect(
        host='localhost',
        user='sept',
        password='your_password',
        database='ayopy'
    )

@report_bp.route('/report')
def report():
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = '''
    SELECT 
    t.kode_transaksi,
    a.nama_anggota AS anggota_nama,
    ad.nama_anggota AS admin_nama,
    t.nama_barang,
    t.qty,
    t.harga,
    (t.qty * t.harga) AS total
    FROM 
    tbayotransaksi t
    inner JOIN 
    tbayoanggota a ON t.no_anggota = a.no_anggota
    JOIN 
    tbayoadmin ad ON t.no_admin = ad.no_anggota;

    '''
    cursor.execute(query)
    report_data = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return render_template('report.html', report_data=report_data)
