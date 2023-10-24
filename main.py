class Pile:
    def __init__(self):
        self._liste = []

    def push(self, val):
        self._liste.append(val)

    @property
    def top(self):
        if not self.is_empty:
            return self._liste[-1]
        else:
            return None

    @property
    def size(self):
        return len(self._liste)

    def pop(self):
        if not self.is_empty:
            return self._liste.pop()
        else:
            return None

    @property
    def is_empty(self):
        return len(self._liste) == 0

class File:
    def __init__(self):
        # Initialisation de la file en utilisant une liste vide.
        self._liste = []

    def enqueue(self, element):
        # Ajoute un élément à la fin de la file.
        self._liste.append(element)

    def dequeue(self):
        # Retire et renvoie l'élément à l'avant de la file (le premier élément ajouté).
        if not self.is_empty:  # Vérifie si la file n'est pas vide.
            return self._liste.pop(0)
        else:
            return None  # Renvoie None si la file est vide.

    def front(self):
        # Renvoie l'élément à l'avant de la file sans le retirer.
        if not self.is_empty:  # Vérifie si la file n'est pas vide.
            return self._liste[0]
        else:
            return None  # Renvoie None si la file est vide.

    def rear(self):
        # Renvoie l'élément à l'arrière de la file sans le retirer.
        if not self.is_empty:  # Vérifie si la file n'est pas vide.
            return self._liste[-1]
        else:
            return None  # Renvoie None si la file est vide.

    @property
    def size(self):
        # Propriété en lecture seule qui renvoie la taille actuelle de la file.
        return len(self._liste)

    @property
    def is_empty(self):
        # Propriété en lecture seule qui renvoie True si la file est vide, sinon False.
        return len(self._liste) == 0

def test_pile():
    # Pile
    p = Pile()
    p.push(3)
    print("Sommet de la pile:", p.top)
    print("Taille de la pile:", p.size)
    popped_value = p.pop()
    print("Élément retiré de la pile:", popped_value)
    print("La pile est vide:", p.is_empty)


def test_file():
    # File
    f = File()  # Instancie une file vide

    # Ajout d'éléments à la file
    f.enqueue(1)
    f.enqueue(2)
    f.enqueue(3)

    # Affichage de la taille de la file
    print("Taille de la file:", f.size)  # Devrait afficher 3

    # Retrait d'éléments de la file
    front_element = f.dequeue()  # Retire et renvoie le premier élément
    print("Élément à l'avant de la file:", front_element)  # Devrait afficher 1
    print("Nouvelle taille de la file:", f.size)  # Devrait afficher 2

    # Vérification de l'élément à l'arrière de la file
    rear_element = f.rear()
    print("Élément à l'arrière de la file:", rear_element)  # Devrait afficher 3

    # Vérification si la file est vide
    is_empty = f.is_empty
    print("La file est vide:", is_empty)  # Devrait afficher False

def main():
    test_pile()
    print()
    test_file()

if __name__ == "__main__":
    main()  