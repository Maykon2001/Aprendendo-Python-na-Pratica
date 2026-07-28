# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Informe a largura da parede: "))
a = float(input("Informe a altura da parede: "))

area = l * a
tinta = area / 2

print("Sua parede tem dimensão de {} x {} e sua área é de {:.2f}m².".format  (l, a, area))
print("Para pintar essa parede, voçê precisará de {:.2f} litros de tinta.".format(tinta))