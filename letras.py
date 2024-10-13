def verifica_letra_a(texto):
    # Contar o número de 'a' e 'A' na string
    quantidade_a = texto.lower().count('a')

    # Verificar a existência e quantidade de 'a' ou 'A'
    if quantidade_a > 0:
        return f"A letra 'A/a' aparece {quantidade_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."


# Solicita uma string do usuário
texto_usuario = input("Digite uma string: ")
print(verifica_letra_a(texto_usuario))