import textwrap

texto = "Esto es un texto muy la."
#El problema pide que independiente del tamaño se parta el texto
def wrap(string, max_width):
    
    return ("\n".join(textwrap.wrap(string, max_width)))
    
    

print(wrap(texto,10))

