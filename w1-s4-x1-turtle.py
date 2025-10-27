# =============================================================================
# SECTION 1: MODULE TURTLE ET FONCTION DE DESSIN
# =============================================================================

# Importation du module turtle pour dessiner des formes géométriques
import turtle

def square(length):
    """
    Fonction qui dessine un carré avec la tortue graphique
    
    Args:
        length (int/float): La longueur du côté du carré
    
    Principe: Un carré a 4 côtés égaux et 4 angles droits (90°)
    """
    # Boucle pour dessiner les 4 côtés du carré
    for side in range(4):
        turtle.forward(length)  # Avancer de 'length' pixels
        turtle.left(90)         # Tourner à gauche de 90 degrés

# turtle.reset()   # Commande pour effacer le dessin et repositionner la tortue
# square(200)      # Appel de la fonction pour dessiner un carré de 200 pixels

# =============================================================================
# SECTION 2: TYPES DE DONNÉES
# =============================================================================

# Vérification du type de la valeur 1 (entier)
print(type(1))  # Affiche: <class 'int'>

# =============================================================================
# SECTION 3: FONCTIONS AVEC ARGUMENTS VARIABLES (*args)
# =============================================================================

def somme(*largs):
    """
    Fonction qui calcule la somme de tous ses arguments
    
    Args:
        *largs: Nombre variable d'arguments (tuple d'arguments)
    
    Returns:
        La somme de tous les arguments reçus
    
    Note: *largs permet de recevoir un nombre variable d'arguments
    """
    # Si aucun argument n'est fourni, retourner 0
    if not largs:
        return 0
    
    # Initialiser le résultat avec le premier argument
    result = largs[0]
    
    # Additionner tous les arguments suivants
    for i in range(1, len(largs)):
        result += largs[i]
    
    return result

# Test de la fonction avec des listes
liste1 = ['a', 'b', 'c']        # Liste de chaînes de caractères
liste2 = [0, 20, 30]            # Liste d'entiers
liste3 = ['spam', 'eggs']       # Liste de chaînes de caractères

# Attention: Ici on passe 3 listes, donc somme() va concaténer les listes
print(somme(liste1, liste2, liste3))  # Résultat: ['a', 'b', 'c', 0, 20, 30, 'spam', 'eggs']

# =============================================================================
# SECTION 4: NOMBRES COMPLEXES
# =============================================================================

# Différentes façons d'écrire un nombre complexe en Python
# En mathématiques: 3 + 2i, en Python: 3 + 2j (j = unité imaginaire)
c = 3+2j          # Forme la plus simple
c = 3 + 2 * 1j    # Forme explicite avec multiplication
c = 3 + 2.j       # Avec point décimal
c = 3 + 2 * 1.j   # Attention: syntaxe incorrecte en Python!

# =============================================================================
# SECTION 5: OPÉRATIONS ARITHMÉTIQUES
# =============================================================================

# Calcul de puissance: 2 élevé à la puissance 16
print(2 ** 16)  # Résultat: 65536 (2^16)

# =============================================================================
# SECTION 6: CARACTÈRES UNICODE
# =============================================================================

# Affichage de caractères Unicode en utilisant leur code
print("\u03a6")  # Affiche: Φ (phi majuscule grec)
print("\u0556")  # Affiche: Ֆ (caractère arménien)

# =============================================================================
# SECTION 7: GUILLEMETS DANS LES CHAÎNES
# =============================================================================

# Utilisation de guillemets simples pour inclure des guillemets doubles
print('spam"')   # Affiche: spam"

# =============================================================================
# SECTION 8: MÉTHODES DE CHAÎNES ET INDEXATION
# =============================================================================

chaine = "douarnenez"

# Test pour vérifier la position du caractère 'z'
# chaine.index('z') retourne l'index de 'z' dans la chaîne (9)
# len(chaine) retourne la longueur de la chaîne (10)
print(chaine.index('z') == len(chaine))      # False car 9 ≠ 10
print(chaine.index('z') == len(chaine) - 1)  # True car 9 = 10-1 (dernier caractère)

# =============================================================================
# SECTION 9: LISTES ET RÉFÉRENCES D'OBJETS
# =============================================================================

# Démonstration importante: les variables stockent des références aux objets
i = 6

# Création d'une liste contenant différents types de données
a = [i, "j", 3.14, [1, 2, 3]]  # Liste mixte: entier, chaîne, float, liste
print(a)  # Affiche: [6, 'j', 3.14, [1, 2, 3]]

# Modification de la variable i
i = 7

# IMPORTANT: a[0] reste 6 car la liste a stocké la VALEUR de i (6), pas la variable i
print(a)  # Affiche encore: [6, 'j', 3.14, [1, 2, 3]]

# =============================================================================
# SECTION 10: MODIFICATION DE LISTES
# =============================================================================

# Deux façons d'insérer un élément dans une liste:
# a.insert(1, "k")    # Méthode 1: insert() pour insérer à l'index 1
a[2:3] = ["k"]        # Méthode 2: slice assignment (remplace l'élément à l'index 2)

# Retrait du premier élément de la liste
suivant = a.pop(0)    # pop(0) retire et retourne le premier élément
# Équivalent à: suivant = a[0]; del a[0]

print(a)        # Liste après modification
print(suivant)  # Élément retiré

# =============================================================================
# SECTION 11: TRI DE LISTES
# =============================================================================

# Liste de nombres non triés
b = [5, 9, 3, 4, 8, 2, 1, 7, 6, 0]

# Différentes méthodes pour trier en ordre décroissant:
# b = sorted(b, reverse=True)  # Méthode 1: sorted() retourne une nouvelle liste
# b.sort(); b.reverse()        # Méthode 2: trier puis inverser
b.sort(reverse=True)           # Méthode 3: trier directement en ordre décroissant

print(b)  # Affiche: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# print(dir(list))  # Commande pour voir toutes les méthodes disponibles sur les listes

# =============================================================================
# SECTION 12: STRUCTURES CONDITIONNELLES
# =============================================================================

# Test conditionnel simple (toujours vrai dans ce cas)
if 1 < 2:
    print('oui')  # Cette ligne sera toujours exécutée
else:
    print('non')  # Cette ligne ne sera jamais exécutée

# =============================================================================
# SECTION 13: CONVERSION DE TYPES ET JOINTURE
# =============================================================================

# Construction d'une liste en convertissant tous les éléments en chaînes
a = []
for n in [1, 2, '3', 4, 'FIN']:  # Liste mixte: entiers et chaînes
    a.append(str(n))              # Convertir chaque élément en chaîne
print(",".join(a))                # Joindre tous les éléments avec des virgules
                                  # Résultat: "1,2,3,4,FIN"

# =============================================================================
# SECTION 14: FONCTION DE CONVERSION ET JOINTURE
# =============================================================================

# Nouvelle liste pour l'exemple suivant
a = [1, 2, 3, 4, 5]

def to_str(a):
    """
    Fonction qui convertit une liste en chaîne de caractères
    
    Args:
        a (list): Liste d'éléments à convertir
    
    Returns:
        str: Chaîne avec tous les éléments séparés par des espaces
    """
    tmp = []                    # Liste temporaire pour stocker les chaînes
    for i in a:                # Parcourir chaque élément
        tmp.append(str(i))     # Convertir en chaîne et ajouter à tmp
    return " ".join(tmp)       # Joindre avec des espaces

# Test de la fonction avec une liste contenant une seule chaîne
print(to_str(['123']))  # Résultat: "123"

# =============================================================================
# SECTION 15: COMPRÉHENSIONS DE LISTES (LIST COMPREHENSIONS)
# =============================================================================

# Liste d'entrée pour les exemples
entree = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Deux versions de compréhension de liste:
# carres = [x**2 for x in entree]                    # Version 1: tous les carrés
carres = [x**2 for x in entree if x % 3 == 0]       # Version 2: carrés des multiples de 3

print(carres)  # Résultat: [9, 36, 81] (carrés de 3, 6, 9)

# Test du modulo: 6 divisé par 3 donne un reste de 0
print(6 % 3)   # Résultat: 0 (6 est divisible par 3)

# =============================================================================
# SECTION 16: MODULE RANDOM - GÉNÉRATION DE NOMBRES ALÉATOIRES
# =============================================================================

# Importation du module pour la génération de nombres aléatoires
import random

# Affichage des informations sur le module
print(random)                  # Affiche: <module 'random' from '...'>
# help(random)                 # Commande pour voir la documentation complète
print(dir(random))             # Liste toutes les fonctions du module random
# help(random.randint)         # Documentation spécifique de randint

# Génération d'un nombre aléatoire entre 1 et 100 (inclus)
random.randint(1, 100)         # Note: ce nombre n'est pas affiché car pas dans print()

# =============================================================================
# SECTION 17: ÉCRITURE DE FICHIERS
# =============================================================================

# Ouverture d'un fichier en mode écriture
# 'w' = write (écriture), 'r' prefix = raw string (évite les problèmes avec \)
f = open(r'spam.txt', 'w', encoding='utf8')

# Écriture de 100 lignes dans le fichier
for i in range(100):
    f.write(f"ligne {i+1}\n")  # f-string pour formater le texte

# IMPORTANT: Toujours fermer le fichier après utilisation
f.close()

# Vérification du type de l'objet fichier
print(type(f))  # Affiche: <class '_io.TextIOWrapper'>

# Lecture et affichage du contenu du fichier (version commentée)
# with open('spam.txt', 'r', encoding='utf8') as f:
#     print(f.read())  # with garantit la fermeture automatique du fichier

# =============================================================================
# SECTION 18: TRAITEMENT DE FICHIERS - LECTURE ET TRANSFORMATION
# =============================================================================

# Ouverture de deux fichiers: un en lecture, un en écriture
f = open(r'spam.txt', 'r', encoding='utf8')    # Fichier source (lecture)
f2 = open(r'spam2.txt', 'w', encoding='utf8')  # Fichier destination (écriture)

# Traitement ligne par ligne
for line in f:                    # Itération sur chaque ligne du fichier
    line = line.split()           # Découpage de la ligne en mots (liste)
    line[0] = line[0].upper()     # Conversion du premier mot en majuscules
    f2.write(",".join(line) + "\n")  # Écriture avec virgules comme séparateurs

# Fermeture des deux fichiers
f.close()
f2.close()

# Version alternative avec 'with' (recommandée - gestion automatique des fichiers)
# with open(r'spam.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         print(line)

# =============================================================================
# SECTION 19: FICHIERS BINAIRES
# =============================================================================

# Écriture d'un fichier binaire avec 'with' (bonne pratique)
with open(r'spam.bin', 'bw') as f:  # 'bw' = binary write
    for i in range(100):
        f.write(b'\x3d')            # Écriture du byte 0x3D (caractère '=') 100 fois

# =============================================================================
# SECTION 20: TUPLES ET DÉSTRUCTURATION
# =============================================================================

# Création d'un tuple (structure de données immutable)
triple = (1, 2, 3,)  # La virgule finale est optionnelle mais recommandée

# Longueur du tuple
print(len(triple))   # Résultat: 3

# Expression complexe d'indexation imbriquée
# [(1,)] crée une liste contenant un tuple
# [0] accède au premier élément de la liste (le tuple (1,))
# [0] accède au premier élément du tuple (la valeur 1)
print([(1,)][0][0] == 1)  # Résultat: True

# =============================================================================
# SECTION 21: DÉSTRUCTURATION DE TUPLES COMPLEXES
# =============================================================================

# Tuple complexe contenant différents types de données
quadruple = (1, [2, 3], True, [(4,)])
#            |    |      |      |
#          int  liste  bool  liste contenant un tuple

# Tentatives de déstructuration (les versions commentées ne fonctionnent pas):
# ( one, (two, three), ignored, ( ( four ) ) ) = quadruple  # Erreur: types incompatibles
# ( one, (two, three,), _, ( ( four, ), ) ) = quadruple    # Erreur: structure incorrecte

# Déstructuration correcte qui respecte les types:
(one, (two, three), _, [[four]]) = quadruple
#  |      |     |    |     |
# int   liste  bool var  int (dans liste dans liste)

# Affichage des variables extraites
print(one, two, three, four)  # Résultat: 1 2 3 4

# =============================================================================
# FIN DU FICHIER D'EXERCICES
# =============================================================================