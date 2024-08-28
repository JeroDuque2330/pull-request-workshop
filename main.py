# El siguiente programa recibe una entrada (input) del usuario y retorna el número de dígitos y de letras que contenga el mismo

# Itendifica los errores y modifica el programa para que funcione según el enunciado
user_input = input ("NGRESA UN USUARIO CON NUMEROS Y LETRAS")

digits = 0
letters = 0

for i in user_input:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1

print(" The input string", user_input, "has", letters, "letters and", digits, "digits.")
