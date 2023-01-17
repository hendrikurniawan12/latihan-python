#menginput angka
angka = int(input("masukan angka: "))

#jika habis bilangan Nol, maka genap
if (angka % 2) ==0:
    print("{0} adalah bilangan genap".format(angka))

#jika tidak habis dibagi nol maka ganjih
else:
    print("{0}adalah bilangan ganjil".format(angka))