# README - Code pour la Pile et la File

Ce projet consiste en deux classes Python, `Pile` et `File`, qui sont des structures de données de base utilisées pour gérer des collections d'éléments.

## Table des matières

1. [Introduction](#introduction)
2. [Fonctionnalités](#fonctionnalités)
3. [Exigences](#exigences)
4. [Installation](#installation)
5. [Utilisation](#utilisation)
6. [Exemples](#exemples)
7. [Contribution](#contribution)
8. [Auteurs](#auteurs)
9. [Licence](#licence)

## Introduction

Les classes `Pile` et `File` sont implémentées en Python et offrent des fonctionnalités de base pour ajouter, retirer, et accéder à des éléments. La classe `Pile` est une structure de données de type pile (Last In, First Out), tandis que la classe `File` est une structure de données de type file (First In, First Out).

## Fonctionnalités

Les fonctionnalités clés de ces classes comprennent :

- Pour la classe `Pile` :
  - `push(val)`: Ajoute un élément à la pile.
  - `pop()`: Retire et renvoie l'élément au sommet de la pile.
  - `top`: Propriété qui renvoie l'élément au sommet de la pile.
  - `size`: Propriété qui renvoie la taille de la pile.
  - `is_empty`: Propriété qui indique si la pile est vide.

- Pour la classe `File` :
  - `enqueue(val)`: Ajoute un élément à la file.
  - `dequeue()`: Retire et renvoie l'élément à l'avant de la file.
  - `front`: Propriété qui renvoie l'élément à l'avant de la file.
  - `rear`: Propriété qui renvoie l'élément à l'arrière de la file.
  - `size`: Propriété qui renvoie la taille de la file.
  - `is_empty`: Propriété qui indique si la file est vide.

## Exigences

Ce code ne nécessite que Python 3.x pour fonctionner. Aucune autre dépendance n'est requise.

## Installation

1. Téléchargez ou clonez ce dépôt sur votre ordinateur.
2. Assurez-vous d'avoir Python 3.x installé sur votre système.

## Utilisation

Pour utiliser les classes `Pile` et `File` dans votre propre code, vous pouvez simplement les importer et les instancier. Par exemple :

```python
from pile_file import Pile, File

# Utilisation de la Pile
p = Pile()
p.push(3)
print(p.top)
print(p.size)
print(p.pop())
print(p.is_empty)

# Utilisation de la File
f = File()
f.enqueue(1)
f.enqueue(2)
print(f.front)
print(f.rear)
print(f.dequeue())
```

## Exemples

Consultez les exemples fournis dans le code pour des cas d'utilisation spécifiques des classes `Pile` et `File.

## Contribution

Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre des pull requests ou à signaler des problèmes (issues) sur le dépôt GitHub.

## Auteurs

- Les IDIA3

## Licence

Ce projet est sous licence [LICENSE](LICENSE).
# ASD_24-10-2023
