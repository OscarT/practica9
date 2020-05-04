#comentario de una sola linea
"""
comentario de varias lineas

"""

print("Hola Mundo")
x = 10
print(x)
x = y = z = 2.3
print(x, y, z)
print(type(x))
x = "cadena"
print(type(x)) 

c1 = "Hola"
c2 = "Oscar"
saludo = c1 +" "+c2
print(saludo)

saludo2 = "{} {} {}".format(c1, c2, 3)
print(saludo2)

saludo3 = "Cambio de orden {1} {2} {0}".format(c1, c2, 3)
print(saludo3)