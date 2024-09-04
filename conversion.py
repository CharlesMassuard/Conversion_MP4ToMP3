from moviepy.editor import *
import os
import argparse

def convertisseur(convert_ytdlp = False):
    for nom in os.listdir("."):
        chemin = os.path.join(".", nom)
        if os.path.isfile(chemin) and chemin.endswith(".mp4"):
            clip = VideoFileClip(chemin)
            if(convert_ytdlp):
                nom_fichier = os.path.basename(chemin)[:-18] # Récupère le nom du fichier sans l'extension et le suffixe ajouté par ytdlp
            else:
                nom_fichier = os.path.basename(chemin)[:-4]  # Récupère le nom du fichier sans l'extension
            clip.audio.write_audiofile(nom_fichier + ".mp3")
            clip.close()  # Ferme le clip vidéo
            os.remove(chemin)  # Supprime le fichier original
            
if(__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="Convertisseur de fichiers vidéo en audio")
    parser.add_argument("convert_ytdlp", type=bool, nargs='?', default=False, help="Mettre à True pour enlever le suffixe de 18 caractères ajoutés par yt-dlp (ressemblant à ' [ApjLOC4vcFA]')")
    args = parser.parse_args()
    convertisseur(args.convert_ytdlp)
                                                                             
#                     %((#                                            
#                 #@@@@#&(@(#                                         
#              //,.&%%*&@(&@&&                                        
#    .@&&@@@%*,/...**#*@%@#&#&. %                                     
#    /@@@@%*.##(((%%&%&@&&@(%& # /.                                   
#               %*%#@&@@*&@&%%
#                  &&@%.*@%(%
#                  @&#@%/@&#
#                &&@&##&#&
#               &&,&#/#&%.
#             ((%@&*@&%@.#,%,,Charles Massuard,,*(%##((%((#
#            %@@#&&@@%&&&*,,*.&%%&%&&&@&(#&&(&(#,//%&///,/*/##
#           #&&@%#&&(@&@%@@%&%%&@%(%&@&(&(&#&(%%@&&&***(%%/**
#           *%@@@@@%@%%#%@%&&,#((#/&##%#&#%#&&###@@&#% ,#&&
#            (%@&@@%###&@%*%/%,**&@*,*,%%&#&%%%##&&%(#,,%
#             %&@@@#(%@&%@#@/,%/,@#&# ,,,,@%%%@&#&@%@&&
#              #%&@@%#@@@@@#(/#**%, %%.%&@#@&##&&&@#/
#               /&&&@#&(&@@&@@%.@(&&(,%# ,*%%&&@@&%/
#                  (%@&&@&%@@@@&(% #,/ #,,*%@@&&#/
#                     /%%&&@@&@&@&@@@&&@@#&@&@&,
#                         ,,@#&&&@&@@@@&#%&&%#%,
#                           /@@@@@#@&&@@@@@@@@&,
#                            %&@&,,*****(%#&&,
#                          #&&&,********%&&,
#                        /&&&,,********%(&,
#                %&&&&&&&&&&&%&*******&/%,
#                            @@/###((%#%&//
#                      ////((((((((////