def potenciaR (num,exp):
    if(exp > 1):
        return num * potenciaR(num,exp-1)
    else:
        if(exp == 0):
            return 1
        else:
            return num
        
print(potenciaR(10,2))