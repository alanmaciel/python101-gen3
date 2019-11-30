# Verifica que el nombre sea "Elsa" o  que el nombre no sea igual a Luis y que no tenga 17 años al mismo tiempo, combina las palabras clave 'and', 'or' y ‘not'.:

name = "Luis"
age = 17

print(name == "Luis" or not age > 17)
print(name == "Luis" or not age > 17)

print(name == "Elsa" or not (name == "Luis" and age == 17) )
#"name" es "Elsa" or not ("name" equal "Luis" and he is 17 years old))
