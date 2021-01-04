# -*- coding: utf-8 -*-
"""
                           Projet Splaby'O
        Projet Python 2020-2021 de 1ere année et AS DUT Informatique Orléans

"""
from carte import *
from participants import *
from matrice import *
import random


def Plateau(les_joueurs, taille=7, nb_objets=3):
    """
    créer un nouveau plateau contenant les joueurs passés en paramètres

    :param les_joueurs: la liste des joueurs participant à la partie
    :param taille: un entier qqui donne la taille du labyrinthe
    :param nb_objets: un entier qui indique combien d'objets différents existent
    :return: un couple contenant
              * une matrice de taille taillextaille représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              * la carte amovible qui n'a pas été placée sur le plateau
    """
    matrice = Matrice(taille, taille)
    joueurs = les_joueurs["joueurs"].copy()

    coins = {(0, 0): Carte(True, False, False, True),
             (0, get_nb_colonnes(matrice) - 1): Carte(True, True, False, False),
             (get_nb_lignes(matrice) - 1, get_nb_lignes(matrice) - 1): Carte(False, True, True, False),
             (get_nb_lignes(matrice) - 1, 0): Carte(False, False, True, True)}
    for (coord, carte) in coins.items():
        if len(joueurs) > 0:  # get_nb_joueurs
            poser_joueur(carte, joueurs.pop(-1)) #[joueur1, joueur2, ..., joueurN], joueurs.pop(-1) -> joueurN & joueurs = [joueur1, joueur2, ..., joueurN-1]

        set_valeur(matrice, coord[0], coord[1], carte)

    set_valeur(matrice, 0, 2, Carte(True, False, False, False))
    set_valeur(matrice, 0, 4, Carte(True, False, False, False))

    set_valeur(matrice, 2, 0, Carte(False, False, False, True))
    set_valeur(matrice, 2, 2, Carte(False, False, False, True))
    set_valeur(matrice, 2, 4, Carte(True, False, False, False))
    set_valeur(matrice, 2, 6, Carte(False, True, False, False))

    set_valeur(matrice, 4, 0, Carte(False, False, False, True))
    set_valeur(matrice, 4, 2, Carte(False, False, True, False))
    set_valeur(matrice, 4, 4, Carte(False, True, False, False))
    set_valeur(matrice, 4, 6, Carte(False, True, False, False))

    set_valeur(matrice, 6, 2, Carte(False, False, True, False))
    set_valeur(matrice, 6, 4, Carte(False, False, True, False))

    cartes_amovibles = creer_cartes_amovibles()

    for i in range(taille):
        for j in range(taille):
            if i % 2 == 1 or j % 2 == 1:
                set_valeur(matrice, i, j, cartes_amovibles.pop(-1))

    poser_les_objets(matrice, len(les_joueurs["joueurs"]), nb_objets)

    return (matrice, cartes_amovibles.pop(-1))


def creer_cartes_amovibles():
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu 
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées

    :return: la liste mélangée aléatoirement des cartes amovibles créees
    """
    cartes = []
    compteur_angles = 4
    compteur_jonctions = 12
    compteur_couloirs = 0

    while compteur_angles != 20:
        angles = [Carte(True, False, False, True), Carte(True, True, False, False), Carte(False, True, True, False),
                  Carte(False, False, True, True)]
        r2 = random.randint(0, 3)
        cartes.append(angles[r2])
        compteur_angles += 1

    while compteur_couloirs != 12:
        cartes.append(Carte(False, True, False, True))
        compteur_couloirs += 1

    while compteur_jonctions != 18:
        cartes.append(Carte(False, False, False, True))
        compteur_jonctions += 1

    random.shuffle(cartes)
    return cartes


def poser_les_objets(plateau, nb_joueurs, nb_objets):
    """
    cette fonction va poser de manière aléatoire les objets sur le plateau, il y aura un objet de chaque types par joueur

    :param plateau: le plateau
    :param nb_joueurs: un entier indiquant le nombre de joueurs participant à la partie
    :param nb_objets: un entier le nombre de type d'objets diffé    cpt = 0rents
    :return: cette fonction ne retourne rien mais modifie le plateau
    """
    for obj in range(nb_objets):
        for i in range(nb_joueurs):
            carte = None
            while carte is None or get_objet(carte) != 0:
                random_i = random.randint(0, get_nb_lignes(plateau) - 1)
                random_j = random.randint(0, get_nb_colonnes(plateau) - 1)
                carte = get_valeur(plateau, random_i, random_j)

            poser_objet(carte, obj + 1)





def get_coordonnees_joueur(plateau, joueur):
    """'
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre

    :param plateau: le plateau considéré
    :param joueur: le joueur à trouver
    :return: un couple d'entiers donnant les coordonnées du joueur ou None si le joueur n'est pas sur le plateau
    """
    matrice = plateau
    for i in range(get_nb_lignes(matrice)):
        for j in range(get_nb_colonnes(matrice)):
            carte = get_valeur(matrice, i, j)
            if possede_joueur(carte, joueur):
                return (i, j)

    return None


def get_voisins(plateau, lig, col):
    matrice = plateau
    voisins = dict()
    if 0 <= lig - 1 < get_nb_lignes(matrice):
        voisins["N"] = (lig - 1, col)

    if 0 <= col - 1 < get_nb_colonnes(matrice):
        voisins["O"] = (lig, col - 1)

    if 0 <= col + 1 < get_nb_colonnes(matrice):
        voisins["E"] = (lig, col + 1)

    if 0 <= lig + 1 < get_nb_lignes(matrice):
        voisins["S"] = (lig + 1, col)

    return voisins


def passage_plateau(plateau, lig, col, direction):
    """
    indique si il y a bien un passage dans le direction passée en paramètre à partir de la position
    lig,col sur le plateau. La fonction retourne None si il n'y a pas de passage ou les coordonnées
    de la case où on arrive en prenant le passage s'il y en a un

    :param plateau: le plateau
    :param lig: un entier donnant le numéro de la ligne
    :param col: un entier donnant le numéro de la colonne
    :param direction: un caractère 'N', 'S', 'O' ou 'E' indiquant la direction où on veut aller
    :return: None s'il n'y a pas de passage possible
             (x,y) les coordonnées où on arrive en prenant le passage s'il existe (un couple d'entiers)
    """
    matrice = plateau
    voisins = get_voisins(plateau, lig, col)
    carte = get_valeur(matrice, lig, col)
    cardinalites = ["N", "E", "S", "O"]
    for cardinalite in cardinalites:
        if direction == cardinalite and cardinalite in voisins.keys():
            i_direction, j_direction = voisins[cardinalite]
            carte_direction = get_valeur(matrice, i_direction, j_direction)
            if (cardinalite == "N" and passage_nord(carte, carte_direction)) or (
                    cardinalite == "E" and passage_est(carte, carte_direction)) or (
                    cardinalite == "S" and passage_sud(carte, carte_direction)) or (
                    cardinalite == "O" and passage_ouest(carte, carte_direction)):
                return (i_direction, j_direction)

    return None


def case_adjactente(plateau, lig, col, direction):
    voisins = get_voisins(plateau, lig, col)
    cardinalites = ["N", "E", "S", "O"]
    for cardinalite in cardinalites:
        if direction == cardinalite and cardinalite in voisins.keys():
            i_direction, j_direction = voisins[cardinalite]
            if cardinalite == "N" or cardinalite == "E" or cardinalite == "S" or cardinalite == "O":
                return (i_direction, j_direction)

    return None


def marquage_direct(plateau, calque, cpt, lig_arrivee, col_arrivee):
    """
    marque avec la valeur marque les éléments du calque tel que la valeur
    correspondante n'est pas un mur (de valeur differente de 1) et
    qu'un de ses voisins dans le calque à pour valeur val
    la fonction doit retourner True si au moins une case du calque a été marquée
    """

    case_modifie = False
    for i in range(get_nb_lignes(calque)):
        for j in range(get_nb_colonnes(calque)):
            valeur_case = get_valeur(calque, i, j)
            if valeur_case == cpt:
                for (cardinalite, case_cible) in get_voisins(plateau, i, j).items():
                    if passage_plateau(plateau, i, j, cardinalite) is not None and (
                            valeur_case == 1 or get_valeur(calque, case_cible[0], case_cible[1]) != cpt - 1):
                        set_valeur(calque, case_cible[0], case_cible[1], cpt + 1)
                        case_modifie = True

    return case_modifie


def accessible(plateau, lig_depart, col_depart, lig_arrivee, col_arrivee):
    """
    indique si il y a un chemin entre la case lig_depart,col_depart et la case lig_arrivee,col_arrivee du labyrinthe

    :param plateau: le plateau considéré
    :param lig_depart: la ligne de la case de départ
    :param col_depart: la colonne de la case de départ
    :param lig_arrivee: la ligne de la case d'arrivée
    :param col_arrivee: la colonne de la case d'arrivée
    :return: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    calque = Matrice(7, 7, 0)
    set_valeur(calque, lig_depart, col_depart, 1)

    cpt = 1
    calque_modifie = True
    while calque_modifie:
        if not marquage_direct(plateau, calque, cpt, lig_arrivee, col_arrivee):
            calque_modifie = False
        else:
            if get_valeur(calque, lig_arrivee, col_arrivee) != 0:
                return True

        cpt += 1

    return False


def peindre_direction_couleur(plateau, lig, col, direction, couleur, reserve_peinture, traverser_mur, tester=False):
    """
    Permet de peindre d'un couleur les cases accessibles à partir de lig,col dans la direction direction avec la reserve
    de peinture disponible.
    La fonction retourne la liste des joueurs touchés et le nombre de cases peintes.
    Attention si le paramètre tester est à True les cases ne sont pas réellement peintes (on teste juste combien de
    cases seraient peintes)

    :param plateau: un plateau
    :param lig: ligne de départ
    :param col: colonne de départ
    :param direction: un caractère valeur 'N','E','S' ou 'O'
    :param couleur: une couleur de peinture
    :param reserve_peinture: le nombre maximum de cases pouvant être peinte
    :param traverser_mur: booléen permettant de traverser une fois un mur (pouvoir du pistolet)
    :param tester: booléen indiquant si on souhaite vraiment peindre les cases ou juste tester combien on peut en peindre
    :return: un couple contenant la liste des joueurs touchés lors de l'action de peindre et le nombre de cases peintes
    """
    joueurs_touches = list()
    i_direction = lig
    j_direction = col
    cases_peintes = 0
    bloque = False

    while not bloque and reserve_peinture > 0:
        cases_peintes += 1
        coord_direction = passage_plateau(plateau, i_direction, j_direction, direction)
        carte = get_valeur(plateau, i_direction, j_direction)
        joueurs = get_liste_joueurs(carte)

        #notes : on part du principe qu'un mur contre un mur constitue un seul mur
        if coord_direction is None: #s'il y a un mur
            if traverser_mur:
                coord_adjactente = case_adjactente(plateau, i_direction, j_direction, direction)
                if coord_adjactente is not None:
                    if not tester:
                        set_couleur(carte, couleur)
                        reserve_peinture -= 1

                    i_direction = coord_adjactente[0]
                    j_direction = coord_adjactente[1]
                    traverser_mur = False
                else:
                    if not tester:
                        set_couleur(carte, couleur)
                        reserve_peinture -= 1

                    bloque = True
            else:
                if not tester:
                    set_couleur(carte, couleur)
                    reserve_peinture -= 1

                if not traverser_mur:
                    bloque = True
        else:
            if not tester:
                set_couleur(carte, couleur)
                reserve_peinture -= 1


            i_direction = coord_direction[0]
            j_direction = coord_direction[1]

        joueurs_touches.extend(joueurs)


    return (joueurs_touches, cases_peintes)


def nb_cartes_par_couleur(plateau):
    """
    calcule le nombre de cartes coloriées pour chaque couleur

    :param plateau: le plateau
    :return: un dictionnaire contenant pour chaque couleur présente sur le plateau le nombre de carte de cette couleur
    """
    matrice = plateau
    freq_couleurs = dict()
    for i in range(get_nb_lignes(matrice)):
        for j in range(get_nb_colonnes(matrice)):
            carte = get_valeur(matrice, i, j)
            couleur = get_couleur(carte)
            if couleur != 'aucune':
                if couleur in freq_couleurs:
                    freq_couleurs[couleur] += 1
                else:
                    freq_couleurs[couleur] = 1

    return freq_couleurs


def affiche_plateau(plateau):
    """
    affichage redimentaire d'un plateau

    :param plateau: le plateau
    :return: rien mais affiche le plateau
    """
    remplissage = ' ' * 30
    print(remplissage, end='')
    for i in range(1, 7, 2):
        print(" " + str(i), sep='', end='')
    print()
    for i in range(get_nb_lignes(plateau[0])):
        print(remplissage, end='')
        if i % 2 == 0:
            print(' ', sep='', end='')
        else:
            print(str(i), sep='', end='')
        for j in range(get_nb_colonnes(plateau[0])):
            print(to_char(get_valeur(plateau[0], i, j)), end='')
        if i % 2 == 0:
            print(' ', sep='', end='')
        else:
            print(str(i), sep='', end='')
        print()
    print(' ', sep='', end='')
    print(remplissage, end='')
    for i in range(1, 7, 2):
        print(" " + str(i), sep='', end='')
    print()


def affiche_ligne_separatrice(matrice, taille_cellule=4):
    '''
    fonction annexe pour afficher les lignes séparatrices
    paramètres: matrice la matrice à afficher
                taille_cellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''
    print()
    for i in range(get_nb_colonnes(matrice) + 1):
        print('-' * taille_cellule + '+', end='')
    print()


def affiche_matrice(matrice, taille_cellule=4):
    '''
    affiche le contenue d'une matrice présenté sous le format d'une grille
    paramètres: matrice la matrice à afficher
                taille_cellule la taille en nb de caractères d'une cellule
    résultat: cette fonction ne retourne rien mais fait un affichage
    '''

    nb_colonnes = get_nb_colonnes(matrice)
    nb_lignes = get_nb_lignes(matrice)
    print(' ' * taille_cellule + '|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_valeur(matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(matrice, taille_cellule)
    print()

# participants = Participants(["joueur1", "joueur2"], ["info", "gea"])
# plateau = Plateau(participants)
# affiche_matrice(plateau[0])
# affiche_plateau(plateau)
# i, j = get_coordonnees_joueur(plateau, Joueur("joueur1", "info"))
