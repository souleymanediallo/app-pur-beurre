# Projet 11 : Améliorez un projet existant en Python

## Contexte du proojet

Il s’agit d’apporter des améliorations de fonctionnalités sur un projet déjà réalisé dans le cadre de ce parcours Python et de corriger des dysfonctionnements signalés par le client sur l’application. J’ai choisi le projet 10, qui est une application Python/Django. Cette application permet à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré ou trop salé". Pour ce faire, plusieurs possibilités d’améliorations s'offrent à moi. J’ai pris l’initiative d’améliorer les points suivants :

* Offrir la possibilité aux utilisateurs de changer leurs mots de passe et leur adresse mail.
* Offrir la possibilité aux utilisateurs de personnaliser leur profil en ajoutant le choix d’une photo.
* L’ajout d’un formulaire de contact pour envoyer un message depuis l’application.


## Liens

* [Lien vers Trello](https://trello.com/b/j1Zc429R/projet-11-améliorez-un-projet-existant-en-python)
* [Lien en ligne ](http://143.110.237.110/)

## Installation

Pour copier le projet en local, ouvrer un terminal et taper les commandes suivantes

```clone
$ git clone https://github.com/souleymanediallo/app-pur-beurre.git
```

Installer un environnement virtuel
```virtualenv
$ pip install virtualenv
```

Créer un environnement virtuel
```venv
$ virtualenv venv
```

Activer l'environnement virtuel
```activate
$ source venv/bin/activate
```

Créer une base de donnée Postgresl
```basededonnee
$ createdb apppurbeurre
```

Créer un fichier .env et renseigner vos variables d'environnement
```environnement
$ touch .env
```

Intaller les dépendances du projet
```installer
$ pip install -r requirements.txt
```

## API
Les données pour tous les produits sont disponibles grâce à l'API Open Food Facts.
Cette API ne nécessite pas l'utilisation d'une clée d'authentification.
La base de données Open Food Facts est disponible sous licence Open Database Licence (Odbl).

Enregistrer les produits dans la base de données en local
```installerdb
$ python manage.py init_db
```

* [Lien OPEN FOOD FACTS](https://fr.openfoodfacts.org/cgi/search.pl)

Demarrer l'application avec la commande suivante

```run
$ python manage.py runserver
```

## Tests

Faire les tests

```test
python manage.py test
```

## Crée avec

* Python 3.8
* Django 3.2
* HTML5 & CSS3
* Bootstrap 5
* Start Bootstrap


## Auteur

Souleymane Diallo
Développeur Python, étudiant openclassrooms

