"""Es un tipo que produce secuencias completas de resultados en lugar de ofrecer un unico valor"""
def gen_basico():
    yield "uno"
    yield "dos"
    yield "tres"

    
for valor in gen_basico():
    print(valor)