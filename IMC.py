persona = {
    "estatura" : 1.76,
    "peso" : 80
}

def imc(peso, estatura):
    return peso/estatura**2

personaIMC = imc(persona["peso"], persona["estatura"])
    
def nivelPeso(personaIMC):
    if personaIMC < 18.5 :
        print("Bajo peso")
    elif personaIMC >=18.5 and personaIMC <= 24.9:
        print("Normal")
    elif personaIMC >= 25.0 and personaIMC <=29.9:
        print("Musculo")
    else:
        print("Obeso")
    
nivelPeso(personaIMC)