def resta(a,b,residuo):
    if(a<0):
        return a,b
    else:
        a = a - b
        residuo = a-b
        resta(a,b,residuo)

print(resta(10,4,0))