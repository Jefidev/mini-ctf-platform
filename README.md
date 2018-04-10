# mini-ctf-platform
Mini CTF platform allowing to create challenges and to submit them. 

## Contenu du fichier mini_ctf_platform/local_settings.py
Ce fichier sert pour le développement et contient le code suivant : 

```
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Créer les équipes pour un CTF
La première chose à faire est de se connecter au shell de Django : 
```
python manage.py shell
```

Les commandes suivantes créeront ensuite 5 équipes aléatoires et en afficheront les données : 
```
>>> from ctf_platform.models import CTF
>>> CTF.create_teams(nb=5)
Team tinyelephant159 created
Team silverswan637 created
Team purplebear200 created
Team bigpanda819 created
Team silverkoala312 created
```

## Terminer un CTF
La première chose à faire est de se connecter au shell de Django : 
```
python manage.py shell
```

Les commandes suivantes désactiveront ensuite toutes les équipes rendant impossible la soumission.

**Il faut noter ici que les équipes disparaitront également du scoreboard. Il est donc nécessaire de 
sauvegarder le scoreboard *AVANT* d'effectuer cette commande** 

```
>>> from ctf_platform.models import CTF
>>> CTF.disable_teams()
```

## Nettoyer la base de données après un CTF
La première chose à faire est de se connecter au shell de Django : 
```
python manage.py shell
```

Les commandes suivantes supprimeront ensuite les équipes et leurs soumissions de flag aux challenges :
```
>>> from ctf_platform.models import CTF
>>> CTF.clear_data()
```

Si vous souhaitez en plus supprimer les challenges, veuillez ajouter la commande suivante : 
```
>>> CTF.clear_challenges()
```