# nltk_Mendoza_Leandro
# Procesamiento de Lenguaje Natural con NLTK

## Datos del alumno

- **Nombre y apellido:** Mendoza Selva Raúl Leandro
- **Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Arficial

## Objetivo del trabajo

Aplicar técnicas básicas de Procesamiento del Lenguaje Natural (PLN) utilizando
la biblioteca NLTK, trabajando sobre comentarios reales obtenidos de un video
de YouTube. El programa descarga comentarios, los tokeniza, normaliza, elimina
puntuación y stopwords, aplica stemming y calcula la frecuencia de palabras
para luego interpretar los resultados obtenidos.

## Video analizado

- **Título:** ¡IMPRESIONANTE VICTORIA DE ARGENTINA PARA METERSE EN 4tos DE FINAL! | Argentina 3–2 Egipto | Resumen
- **URL:** (https://www.youtube.com/watch?v=y85SdAdkLhE&t=143s)

## Cantidad de comentarios descargados

121 comentarios

## Bibliotecas utilizadas

- [nltk](https://www.nltk.org/) — tokenización, stopwords, stemming y frecuencia de palabras
- [youtube-comment-downloader](https://pypi.org/project/youtube-comment-downloader/) — descarga de comentarios de YouTube

## Instrucciones para ejecutar el programa

1. Clonar este repositorio o descargar los archivos `bajar_comentarios.py` y `analizar_comentarios.py`.

2. Instalar las dependencias necesarias:

   ```
   pip install nltk youtube-comment-downloader
   ```

3. Descargar los recursos de NLTK necesarios (solo la primera vez):

   ```
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

4. Editar `bajar_comentarios.py` y reemplazar `VIDEO_URL` por la URL del video a analizar.

5. Ejecutar el script para descargar los comentarios:

   ```
   python bajar_comentarios.py
   ```

   Esto genera el archivo `comentarios_youtube.txt` con los primeros 100 comentarios del video.

6. Ejecutar el script de análisis:

   ```
   python analizar_comentarios.py
   ```

   Esto muestra en consola: el texto original, las oraciones, los tokens, la
   normalización, la eliminación de puntuación y stopwords, la tabla de
   stemming, la frecuencia de palabras, las estadísticas, la interpretación
   de resultados y las conclusiones finales.
