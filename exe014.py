# Exercício Python 014: Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

t = float(input("Informe a temperatura em °C: "))
f = ((9 * t) / 5) + 32
print("A temperatura de {}°C corresponde a {}°F.".format(t, f))