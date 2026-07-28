# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite uma medida em metros: "))

km = medida / 1000
hm = medida / 100
dm = medida / 10
cm = medida * 100
mm = medida * 1000

print("{} metros equivalem a: ". format(medida))
print("Km: {}".format(km))
print("Hm: {}".format(hm))
print("Dm: {}".format(dm))
print("Cm: {}".format(cm))
print("Mm: {}".format(mm))