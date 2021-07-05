# Consigna
# Escribí una función que reciba dos parámetros: un string S y un integer R.

# La función debe devolver un string donde los caracteres consecutivos de S no se repitan más que R veces.

# Tiene que devolver un string con el texto limpio y la cantidad de caracteres repetidos correcta.

# Ejemplos:
# Ej: "AAAAAFFFFOOOA", 2 => "AAFFOOA"
# Ej: "111223333344", 1 => "1234"
# Ej: "AABB", 1 => "AB"

def clean_string(string, max_reps = 2):
    acum = 1
    cleaned_string = string[0]

    for i in range(1, len(string)):
        #comparo la letra actual con la anterior, si son iguales y el valor de acum es menor que el valor de max reps
        #la sumo a cleaned_string
        if(string[i]==string[i-1] and acum < max_reps):
            acum += 1
            cleaned_string += string[i]
        #si la letra actual es distitna a la anterior resteo el acum y la sumo a cleaned_string
        elif(string[i]!=string[i-1]):
            acum = 1
            cleaned_string += string[i]
    print(cleaned_string)


string = "AAAAAFFFFOOOA"
clean_string(string, 2)
string1 = "111223333344"
clean_string(string1, 1)
string2 = "AABB"
clean_string(string2, 1)
