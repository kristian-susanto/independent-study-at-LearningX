from flask import Flask, redirect, url_for, render_template, request

pretest = Flask(__name__)

@pretest.route('/', methods = ['GET'])
def home():
    nama = 'name'
    return render_template('index.html', nama = nama)

@pretest.route('/detail', methods = ['POST'])
def detail():
    merk = request.form['merk']
    processor = request.form['processor']
    ukuran = request.form['ukuran']
    return render_template('detail.html', merk = merk, processor = processor, ukuran = ukuran)

if __name__ == '__main__':
    pretest.run('0.0.0.0', port = 5000, debug = True)