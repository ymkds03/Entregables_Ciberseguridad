def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo."
    return numero ** 0.5