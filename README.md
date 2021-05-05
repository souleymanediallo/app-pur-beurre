# Projet 8 : Créez une plateforme pour amateurs de Nutella

## Contexte

Il s’agit de créer une application web en utilisant le framework Django et l’API OPENFOODFACTS. 
Cette application permettra à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras,
trop sucré, trop salé". Pour ce faire, je crée un algorithme qui va chercher dans ma base de données l’aliment 
qui a un meilleur score nutritionnel à l’aliment demandé et qui est dans la même catégorie. 
Cela nécessite l’utilisation des librairies externes comme Bootstrap ainsi que jQuery. 
L’application doit être responsive,  tester et déployer sur heroku en respectant le cahier des charges.

## Liens

* [Lien Trello](https://trello.com/b/j1Zc429R/projet-8-créez-une-plateforme-pour-amateurs-de-nutella)
* [Lien Heroku](https://app-pur-beurre.herokuapp.com/)

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

Intaller les dépendances du projet
```installer
$ pip install -r requirements.txt
```

## API
Les données pour tous les produits sont disponibles grâce à l'API Open Food Facts.
Cette API ne nécessite pas l'utilisation d'une clée d'authentification.
La base de données Open Food Facts est disponible sous licence Open Database Licence (Odbl).

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


## Auteur

Souleymane Diallo
Développeur Python, étudiant openclassrooms

