def contar_letra_a(texto):
    contador = 0
    for char in texto:
        if char.lower() == 'a':
            contador += 1
    return contador

texto = "Armadilha"

quantidade = contar_letra_a(texto)

if quantidade > 0:
    print(f"A letra 'a' ocorre {quantidade} vezes na string.")
else:
    print("A letra 'a' não ocorre na string.")
