from sys import argv

#leia a seção O que você deve ver para saber como executar isso.
script, first, second = argv

soma = int(first) + int(second)
print("the script is called: ", script)
print(f"A soma é: {soma}")