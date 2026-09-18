universo = {
    "estudiantes": {
        "Juan": ["Logica"],
        "Pedro": [],
        "Pablo": []
    },
    "docentes": {
        "Lourdes": ["Logica"],
        "Dr. Perez": ["Software"],
        "Cisneros": []
    },
    "materias": ["Logica", "Software"],
    "salones": ["207", "208", "209"],
    "becados": ["Juan"]
}

#Predicados
def estudiante(e):
    for estudiantes, materias in universo["estudiantes"].items():
        if estudiantes == e:
            return True
    return False

def docente(d):
    for docentes, materias in universo["docentes"].items():
        if docentes == d:
            return True
    return False

def materia(m):
    for materias in universo["materias"]:
        if materias == m:
            return True
    return False

def salon(s):
    for salones in universo["salones"]:
        if salones == s:
            return True
    return False

def cursa(e, m):
    for estudiantes, materias in universo["estudiantes"].items():
        if estudiantes == e and m in materias:
            return True
    return False

def imparte(d, m):
    for doc, materias in universo["docentes"].items():
        if doc == d and m in materias:
            return True
    return False

def becado(e):
    for estudiantes in universo["becados"]:
        if estudiantes == e:
            return True
    return False


#Consultas
print("1.-  e es un estudiante")
print("Consulta Positiva - Estudiante(Juan):", estudiante("Juan"))
print("Consulta Negativa - ¬Estudiante(Dr. Perez):", estudiante("Dr. Perez"))

print("\n2.- d es un docente")
print("Consulta Positiva - Docente(Dr. Perez):", docente("Dr. Perez"))
print("Consulta Negativa - ¬Docente(Juan):", docente("Juan"))

print("\n3.- m es una materia")
print("Consulta Positiva - Materia(Logica):", materia("Logica"))
print("Consulta Negativa - ¬Materia(207):", materia("207"))

print("\n4.- s  es un salón de clases")
print("Consulta Positiva - Salon(207):", salon("207"))
print("Consulta Negativa - ¬Salon(Logica):", salon("Logica"))

print("\n5.- El estudiante e cursa la materia m")
print("Consulta Positiva - Cursa(Juan, Logica):", cursa("Juan", "Logica"))
print("Consulta Negativa - ¬Cursa(Pablo, Logica):", cursa("Pablo", "Logica"))

print("\n6.- El docente d imparte la materia m")
print("Consulta Positiva - Imparte(Lourdes, Logica):", imparte("Lourdes", "Logica"))
print("Consulta Negativa - ¬Imparte(Dr. Perez, Logica):", imparte("Dr. Perez", "Logica"))

print("\n7.- El estudiante e tiene una beca")
print("Consulta Positiva - Becado(Juan):", becado("Juan"))
print("Consulta Negativa - ¬Becado(Pedro):", becado("Pedro"))