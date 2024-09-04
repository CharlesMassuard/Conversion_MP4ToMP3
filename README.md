# Conversion de fichiers MP4 en MP3

1. Placer ce fichier dans le même répertoire qui les fichiers MP4
2. Pour exectuer la conversion :

    - Si vos fichiers n'ont pas été téléchargés via **yt-dlp** : 
        ```bash
        python ./conversion.py
        ```

    - Si vos fichiers ont été téléchargés via **yt-dlp** et vous souhaitez les convertir *sans* le suffixe :
        ```bash
        python ./conversion.py True
        ```
