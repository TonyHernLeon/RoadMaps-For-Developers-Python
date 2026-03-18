"""
Módulo de Sub-Strings
"""

# Constantes
TEXTO = "ABCDEFGFIJKLMNOPQRSTUVWXYZ"

# Lo normal
fragment0 = TEXTO[2]
print(fragment0)

# Slicing
fragmento_slicing = TEXTO[2:6]
print(f"SubString desde el 2 al 6: {fragmento_slicing}")

fragmento_slicing_al_final = TEXTO[2:]
print(f"SubString desde el 2 al final: {fragmento_slicing_al_final}")

fragmento_slicing_saltando = TEXTO[2:15:3]
print(f"SubString desde el 2 al 13, cada 3 caracteres: {fragmento_slicing_saltando}")

fragmento_slicing_negativo = TEXTO[::-3]
print(f"SubString negativo hasta el inicio caracteres: {fragmento_slicing_negativo}")

texto_al_reves = TEXTO[::-1]
print(f"Abecedario al revés: {texto_al_reves}")
