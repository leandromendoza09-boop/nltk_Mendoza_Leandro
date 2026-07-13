
# Parte 1 - Descargar comentarios de YouTube


from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

VIDEO_URL = "https://www.youtube.com/watch?v=y85SdAdkLhE&t=143s"

downloader = YoutubeCommentDownloader()

print("Descargando comentarios (esto puede tardar un poco)...")

# Trae los comentarios ordenados por los mas populares
comentarios = downloader.get_comments_from_url(
    VIDEO_URL,
    sort_by=SORT_BY_POPULAR
)

# Guardamos los primeros 100 comentarios en un archivo de texto
with open("comentarios_youtube.txt", "w", encoding="utf-8") as archivo:
    for i, comentario in enumerate(comentarios):
        if i >= 100:  # Limite pedido por el TP
            break
        archivo.write(comentario["text"] + "\n")

print("Comentarios descargados correctamente.")
print("Archivo generado: comentarios_youtube.txt")
