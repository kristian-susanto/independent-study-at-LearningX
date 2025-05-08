from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def penjumlahan():
    return render_template('penjumlahan.html')

@app.route('/pengurangan')
def pengurangan():
    return render_template('pengurangan.html')

@app.route('/perkalian')
def perkalian():
    return render_template('perkalian.html')

@app.route('/pembagian')
def pembagian():
    return render_template('pembagian.html')

@app.route('/penjumlahan', methods = ['POST'])
def simpan_penjumlahan():
    angka1 = float(request.form['angka1'])
    angka2 = float(request.form['angka2'])
    hasil = angka1 + angka2
    return jsonify({'pesan' : hasil})

@app.route('/pengurangan', methods = ['POST'])
def simpan_pengurangan():
    angka1 = float(request.form['angka1'])
    angka2 = float(request.form['angka2'])
    hasil = angka1 - angka2
    return jsonify({'pesan' : hasil})

@app.route('/perkalian', methods = ['POST'])
def simpan_perkalian():
    angka1 = float(request.form['angka1'])
    angka2 = float(request.form['angka2'])
    hasil = angka1 * angka2
    return jsonify({'pesan' : hasil})

@app.route('/pembagian', methods = ['POST'])
def simpan_pembagian():
    angka1 = float(request.form['angka1'])
    angka2 = float(request.form['angka2'])
    hasil = angka1 / angka2
    return jsonify({'pesan' : hasil})

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)