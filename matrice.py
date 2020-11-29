# -*- coding: utf-8 -*-
"""
                           Projet Splaby'O
        Projet Python 2020-2021 de 1ere année et AS DUT Informatique Orléans

"""


def Matrice(nb_lignes, nb_colonnes, valeur_par_defaut=0):
    """
    crée une matrice de nb_lignes lignes sur nb_colonnes colonnes en mettant valeur_par_defaut
    dans chacune des cases

    :param nb_lignes: un entier strictement positif qui indique le nombre de lignes
    :param nb_colonnes: un entier strictement positif qui indique le nombre de colonnes
    :param valeur_par_defaut: la valeur par défaut
    :return: la matrice ayant les bonnes propriétés
    """
    ...

def get_nb_lignes(matrice):
    """
    retourne le nombre de lignes de la matrice

    :param matrice: la matrice considérée
    :return: un entier donnant le nombre de lignes
    """
    ...


def get_nb_colonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice

    :param matrice: la matrice considérée
    :return: un entier donnant le nombre de colonnes
    """
    ...


def get_valeur(matrice, ligne, colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice

    :param matrice: la matrice considérée
    :param ligne: le numéro de la ligne (en commençant par 0)
    :param colonne: le numéro de la colonne (en commençant par 0)
    :return: la valeur se trouvant (ligne,colonne) dans la matrice
    """
    ...


def set_valeur(matrice, ligne, colonne, valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    :param matrice: la matrice considérée
    :param ligne: le numéro de la ligne (en commençant par 0)
    :param colonne: le numéro de la colonne (en commençant par 0)
    :param valeur: la valeur à stocker dans la matrice
    :return: cette fonction ne retourne rien mais modifie la matrice
    """
    ...


# ------------------------------------------
# decalages
# ------------------------------------------
def decalage_ligne_a_gauche(matrice, num_ligne, nouvelle_valeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée

    :param matrice: la matrice considérée
    :param num_ligne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    ...
    

def decalage_ligne_a_droite(matrice, num_ligne, nouvelle_valeur=0):
    """
    decale la ligne num_ligne d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne

    :param matrice: la matrice considérée
    :param num_ligne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    ...


def decalage_colonne_en_haut(matrice, num_colonne, nouvelle_valeur=0):
    """
    decale la colonne num_colonne d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne

    :param matrice: la matrice considérée
    :param num_colonne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    ...


def decalage_colonne_en_bas(matrice, num_colonne, nouvelle_valeur=0):
    """
    decale la colonne num_colonne d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne

    :param matrice: la matrice considérée
    :param num_colonne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    ...
