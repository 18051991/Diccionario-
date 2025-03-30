# Crear un diccionario
informacion_personal = {
    "nombre": "Viviana Maribel Ojeda Aviles",
    "edad": 33,
    "ciudad": "El Coca",
    "profesion": "Tecnologias de la Informacion"
}

print("Diccionario original:", informacion_personal)
# Acceder
informacion_personal["ciudad"]="Guayaquil"
print(informacion_personal)

#Añadir clave_valor
# Insertar
informacion_personal["profesion"] = "Tecnologias de la informacion y comunicacion"
print(f"Profesión agregada: {informacion_personal['profesion']}")

# Verificar si la clave "telefono" existe
if "telefono" not in informacion_personal:
    # Agregar la clave "telefono" con un número
    informacion_personal["telefono"] = "0987654329"
    print(f"telefono agregada: {informacion_personal['telefono']}")


# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("La clave 'edad' ha sido eliminada.")
else:
    print("La clave 'edad' no existe en el diccionario.")
# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)