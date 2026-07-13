
# Parte 2 y 3 - Analisis del texto y Conclusiones


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import FreqDist

# ==========================================================
# 1. Mostrar el texto original
# ==========================================================
with open("comentarios_youtube.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("=" * 60)
print("TEXTO ORIGINAL")
print("=" * 60)
print(texto)

# ==========================================================
# 2. Separar el texto en oraciones
# ==========================================================
oraciones = sent_tokenize(texto, language="spanish")

print("\n" + "=" * 60)
print("ORACIONES ENCONTRADAS")
print("=" * 60)
for i, oracion in enumerate(oraciones):
    print(f"Oracion {i + 1}: {oracion}")

# ==========================================================
# 3. Tokenizar el texto
# ==========================================================
tokens = word_tokenize(texto, language="spanish")

print("\n" + "=" * 60)
print("TOKENS")
print("=" * 60)
print(tokens)

# ==========================================================
# 4. Normalizar (minusculas)
# ==========================================================
tokens_minuscula = [token.lower() for token in tokens]

print("\n" + "=" * 60)
print("TOKENS NORMALIZADOS (minusculas)")
print("=" * 60)
print(tokens_minuscula)

# ==========================================================
# 5. Eliminar puntuacion y caracteres especiales
# ==========================================================
palabras = [token for token in tokens_minuscula if token.isalpha()]

print("\n" + "=" * 60)
print("PALABRAS SIN PUNTUACION")
print("=" * 60)
print(palabras)

# ==========================================================
# 6. Eliminar stopwords
# ==========================================================
stop_words = set(stopwords.words("spanish"))

palabras_sin_stopwords = [
    palabra for palabra in palabras if palabra not in stop_words
]

print("\n" + "=" * 60)
print("PALABRAS SIN STOPWORDS")
print("=" * 60)
print(palabras_sin_stopwords)

# ==========================================================
# 7. Aplicar Stemming (tabla de al menos 20 palabras)
# ==========================================================
stemmer = SnowballStemmer("spanish")

print("\n" + "=" * 60)
print("STEMMING (primeras 20 palabras)")
print("=" * 60)
print("Palabra original".ljust(20), "Stem")
print("-" * 35)
for palabra in palabras_sin_stopwords[:20]:
    print(palabra.ljust(20), stemmer.stem(palabra))

stems = [stemmer.stem(palabra) for palabra in palabras_sin_stopwords]

# ==========================================================
# 8. Frecuencia de palabras (20 mas frecuentes)
# ==========================================================
frecuencia = FreqDist(palabras_sin_stopwords)

print("\n" + "=" * 60)
print("20 PALABRAS MAS FRECUENTES")
print("=" * 60)
for palabra, cantidad in frecuencia.most_common(20):
    print(f"{palabra:20} {cantidad}")

# ==========================================================
# 9. Estadisticas
# ==========================================================
vocabulario = set(palabras_sin_stopwords)
stems_diferentes = set(stems)

print("\n" + "=" * 60)
print("ESTADISTICAS")
print("=" * 60)
print("Cantidad de comentarios analizados:", texto.count("\n"))
print("Cantidad de oraciones:", len(oraciones))
print("Cantidad de tokens:", len(tokens))
print("Cantidad de palabras (sin puntuacion):", len(palabras))
print("Cantidad de palabras sin stopwords:", len(palabras_sin_stopwords))
print("Cantidad de palabras diferentes (vocabulario):", len(vocabulario))
print("Cantidad de stems diferentes:", len(stems_diferentes))

# ==========================================================
# 10. Interpretacion de resultados
# ==========================================================
top_5 = frecuencia.most_common(5)

print("\n" + "=" * 60)
print("INTERPRETACION DE RESULTADOS")
print("=" * 60)
print("Las 5 palabras mas frecuentes fueron:")
for palabra, cantidad in top_5:
    print(f" - {palabra} ({cantidad} veces)")

print("\nNOTA: las preguntas de tematica predominante y si el stemming")
print("agrupo bien las palabras se responden en el informe Word,")
print("mirando estos resultados.")

# ==========================================================
# PARTE 3 - CONCLUSIONES
# ==========================================================
print("\n" + "=" * 60)
print("CONCLUSIONES")
print("=" * 60)
print("\nVideo analizado:")
print("¡IMPRESIONANTE VICTORIA DE ARGENTINA PARA METERSE EN 4tos DE FINAL! | Argentina 3–2 Egipto | Resumen")
print("\nCantidad de comentarios:")
print(texto.count("\n"))
print("\nLas palabras mas frecuentes fueron:")
for palabra, cantidad in top_5:
    print(palabra)
print("\nEl stemming permitio agrupar palabras con distintas terminaciones")
print("bajo una misma raiz.")
print("\nLa tematica predominante del video esta relacionada con:")
print("FUBTOL")
