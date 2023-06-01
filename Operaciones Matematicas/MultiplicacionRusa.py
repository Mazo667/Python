def mulRusa(a,b):
    """Multiplicacion Rusa Recursiva"""
    if(a == 1):
        return b
    elif(a % 2 != 0):
        return b + mulRusa(a/2,b*2)
    else:
        return mulRusa(a/2,b*2)
    
print(mulRusa(2,3))