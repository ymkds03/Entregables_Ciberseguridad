def datosINE():
    INE = {}
    INE['NombreINE'] = input("Digita tu nombre: ")
    INE['ApellidoPaINE'] = input("Digita tu apellido paterno: ")
    INE['ApellidoMaINE'] = input("Digita tu apellido materno: ")
    INE['FeNaciINE'] = input("Digita tu fecha de nacimiento. Ej, 10/01/2003: ")
    INE['SexINE'] = input("Digita tu sexo: ")
    INE['ClaveElectorINE'] = input("Digita tu Clave de Elector: ")
    INE['YearRegistroINE'] = input("Digita el año de registro de tu INE. Ej, 2020 00: ")
    INE['VigenciaINE'] = input("Digita la vigencia de tu INE. Ej, 2020-2030: ")
    INE['SeccIne'] = input("Digita tu sección: ")
    INE['DomicilioINE'] = input("Digita tu domicilio: ")
    INE['CURPINE'] = input("Digita tu CURP: ")
    
    return INE

def generarDatos(dataINE, archINE):
    with open(archINE, 'w') as file:
        for clave, valor in dataINE.items():
            file.write(f"{clave}: {valor}\n")

INE = datosINE()

nombreArchivoINE = "DatosDeLaINE.txt"

generarDatos(INE, nombreArchivoINE)
