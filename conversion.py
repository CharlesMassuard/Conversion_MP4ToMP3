from moviepy.editor import *
import os

for nom in os.listdir("."):
    chemin = os.path.join(".", nom)
    if os.path.isfile(chemin) and chemin.endswith(".mp4"):
        clip = VideoFileClip(chemin)
        nom_fichier = os.path.basename(chemin)[:-4]  # Récupère le nom du fichier sans l'extension
        clip.audio.write_audiofile(nom_fichier + ".mp3")
        clip.close()  # Ferme le clip vidéo
        os.remove(chemin)  # Supprime le fichier original