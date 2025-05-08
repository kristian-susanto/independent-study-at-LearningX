# 1. Variable
pohon = "mangga"
tahun = 2023
berat = 20,5
print("Tahun ini adalah tahun: ", tahun)
print(pohon)

# 2. List
car = ['Avanza', 'Pajero', 'Ayla']
car.append('Mobil Dava')
print(car)

# 3. Dictionary
olahraga=[{'kaki':{'futsal','sepakbola','takraw'}, 'tangan':{'voli','basket','lempar lembing','tenis'}},{}]
print(olahraga[0]['tangan'][1])

# 4. Perulangan
for angka in car:
    print(angka)

# 5. Function
def perkalian(x):
    return 10*x

print("Hasil perkalian dengan 10: ", perkalian(10))

def penilaian(nilai):
    if nilai<=100 and nilai>=75:
        print('Lulus')
    elif nilai<75 and nilai>=50:
        print('Remidial')
    else:
        print('Kamu tidak lulus')

penilaian(75)