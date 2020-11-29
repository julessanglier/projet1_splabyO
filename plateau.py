# -*- coding: utf-8 -*-
"""
                           Projet Splaby'O
        Projet Python 2020-2021 de 1ere année et AS DUT Informatique Orléans

"""
from carte import *
from participants import *
from matrice import *


def Plateau(les_joueurs, taille=7, nb_objets=3):
    """
    créer un nouveau plateau contenant les joueurs passés en paramètres

    :param les_joueurs: la liste des joueurs participant à la partie
    :param taille: un entier qqui donne la taille du labyrinthe
    :param nb_objets: un entier qui indique combien d'objets différents existent
    :return: un couple contenant
              * une matrice de taille taillextaill représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              * la carte amovible qui n'a pas été placée sur le plateau
    """
    ...

def creer_cartes_amovibles():
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu 
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées

    :return: la liste mélangée aléatoirement des cartes amovibles créees
    """
    ...

def poser_les_objets(plateau, nb_joueurs, nb_objets):
    """
    cette fonction va poser de manière aléatoire les objets sur le plateau, il y aura un objet de chaque types par joueur

    :param plateau: le plateau
    :param nb_joueurs: un entier indiquant le nombre de joueurs participant à la partie
    :param nb_objets: un entier le nombre de type d'objets différents
    :return: cette fonction ne retourne rien mais modifie le plateau
    """
    ...
    

def get_coordonnees_joueur(plateau, joueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre

    :param plateau: le plateau considéré
    :param joueur: le joueur à trouver
    :return: un couple d'entiers donnant les coordonnées du joueur ou None si le joueur n'est pas sur le plateau
    """
    ...
    

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
    ...


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
    ...
 

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
    ...


def nb_cartes_par_couleur(plateau):
    """
    calcule le nombre de cartes coloriées pour chaque couleur

    :param plateau: le plateau
    :return: un dictionnaire contenant pour chaque couleur présente sur le plateau le nombre de carte de cette couleur
    """
    ...


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
    for i in range(get_nb_lignes(plateau)):
        print(remplissage, end='')
        if i % 2 == 0:
            print(' ', sep='', end='')
        else:
            print(str(i), sep='', end='')
        for j in range(get_nb_colonnes(plateau)):
            print(to_char(get_valeur(plateau, i, j)), end='')
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
