hechos = {
    "animal_1": {
        "tiene_pelo": True,
        "come_carne": True,
        "color_leonado": True,
        "manchas_oscuras": True
    },
    
    "animal_2": {
        "tiene_plumas": True,
        "es_nocturno": True,
        "ojos_frontales": True,
        "tiene_penachos": True
    },
    
    "animal_3": {
        "tiene_pelo": True,
        "tiene_pezuñas": True,
        "da_leche": True,
        "tiene_ubres": True
    },
    
    "animal_4": {
        "tiene_pelo": True,
        "tiene_pezuñas": True,
        "cuernos_grandes": True,
        "robusto": True,
        "tiene_ubres": False
    },
    
    "animal_5": {
        "tiene_plumas": True,
        "vuela": True,
        "pone_huevos": True,
        "es_nocturno": True,
        "cara_corazon": True
    }
}
def tiene(animal, caracteristica):
    return hechos.get(animal, {}).get(caracteristica, False)

# REGLAS DE ANA TORRES
def es_mamifero(a):
    return tiene(a, "tiene_pelo") or tiene(a, "da_leche")

def es_ave(a):
    return tiene(a, "tiene_plumas") or (tiene(a, "vuela") and tiene(a, "pone_huevos"))

def es_carnivoro(a):
    return es_mamifero(a) and tiene(a, "come_carne")

def es_ungulado(a):
    return es_mamifero(a) and tiene(a, "tiene_pezuñas")

def es_guepardo(a):
    return es_carnivoro(a) and tiene(a, "color_leonado") and tiene(a, "manchas_oscuras")

def es_tigre(a):
    return es_carnivoro(a) and tiene(a, "rayas_negras")

def es_jirafa(a):
    return es_ungulado(a) and tiene(a, "cuello_largo") and tiene(a, "manchas_oscuras")

def es_cebra(a):
    return es_ungulado(a) and tiene(a, "rayas_negras")


# REGLAS DE ENTREVISTA MIGUEL
def es_buho(a):
    return es_ave(a) and tiene(a, "es_nocturno") and tiene(a, "ojos_frontales") and tiene(a, "tiene_penachos")

def es_lechuza(a):
    return es_ave(a) and tiene(a, "es_nocturno") and tiene(a, "cara_corazon")


# REGLAS DE ENTREVISTA JOSÉ RAMÓN 
def es_vaca(a):
    return es_ungulado(a) and tiene(a, "tiene_ubres")

def es_toro(a):
    return es_ungulado(a) and tiene(a, "cuernos_grandes") and tiene(a, "robusto") and not tiene(a, "tiene_ubres")


# MOTOR DE INFERENCIA 
def identificar_animal(a):
    if es_guepardo(a): return "Guepardo (Ana Torres)"
    if es_tigre(a):    return "Tigre (Ana Torres)"
    if es_jirafa(a):   return "Jirafa (Ana Torres)"
    if es_cebra(a):    return "Cebra (Ana Torres)"
    if es_buho(a):     return "Búho (Entrevista Miguel V.)"
    if es_lechuza(a):  return "Lechuza (Entrevista Miguel V.)"
    if es_vaca(a):     return "Vaca (Entrevista José P.)"
    if es_toro(a):     return "Toro (Entrevista José P.)"
    return "No clasificado"

if __name__ == "__main__":
    print("=== RESULTADOS DE INFERENCIA ===")
    for animal in hechos:
        resultado = identificar_animal(animal)
        print(f"{animal}: {resultado}")
        
#Se corrigió la estructura de Vaca y Toro a la regla intermedia de UNGULADO en lugar de la regla de MAMÍFERO directamenteme ya que me di cuenta que entran en esa categoría de las reglas.