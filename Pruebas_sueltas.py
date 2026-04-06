def cuantos_dias(mes):
    meses = {
        1 : 31, #Enero
        2 : 28, #Febrero
        3 : 30, #Marzo
        4 : 31, #Abril
        5 : 30 #Mayo
        #Etc...
    }
    if mes > 12:
        return f"el parametro debe ser entre 1-12"
    else:
        return meses[mes]

print(cuantos_dias(13))