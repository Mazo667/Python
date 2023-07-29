"""Empaqueta todos los parametros en uno solo"""
def get_product(**datos):
    print(datos["id"],datos["name"])

get_product(id="23",name="Iphone",desc="Esto es un Iphone")
#Output: 23 Iphone

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')