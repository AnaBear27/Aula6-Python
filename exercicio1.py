#CONTAR VOGAIS

frase = input("Digite uma frase ou uma palavra: ")

vogais = "aeiou"

contador = 0

for caractere in frase:
    if caractere.lower() in vogais:
        contador += 1

print("Números de vogais na frase:", contador)