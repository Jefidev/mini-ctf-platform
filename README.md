# mini-ctf-platform
Mini CTF platform allowing to create challenges and to submit them. 

## Contenu du fichier mini_ctf_platform/local_settings.py
Ce fichier sert pour le développement et contient le code suivant : 

```
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
