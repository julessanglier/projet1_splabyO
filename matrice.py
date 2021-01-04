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
    liste_val = []
    for i in range(nb_lignes):
        liste_val.append([])
        for j in range(nb_colonnes):
            liste_val[i].append(valeur_par_defaut)

    return (nb_lignes, nb_colonnes, liste_val)

def get_nb_lignes(matrice):
    """
    retourne le nombre de lignes de la matrice

    :param matrice: la matrice considérée
    :return: un entier donnant le nombre de lignes
    """
    if matrice == None:
        raise ("Objet matrice nul !")

    return matrice[0]


def get_nb_colonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice

    :param matrice: la matrice considérée
    :return: un entier donnant le nombre de colonnes
    """
    if matrice == None:
        raise ("Objet matrice nul !")

    return matrice[1]


def get_valeur(matrice, ligne, colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice

    :param matrice: la matrice considérée
    :param ligne: le numéro de la ligne (en commençant par 0)
    :param colonne: le numéro de la colonne (en commençant par 0)
    :return: la valeur se trouvant (ligne,colonne) dans la matrice
    """
    if matrice == None:
        raise ("Objet matrice nul !")

    liste_val = matrice[2]
    return liste_val[ligne][colonne]


def set_valeur(matrice, ligne, colonne, valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    :param matrice: la matrice considérée
    :param ligne: le numéro de la ligne (en commençant par 0)
    :param colonne: le numéro de la colonne (en commençant par 0)
    :param valeur: la valeur à stocker dans la matrice
    :return: cette fonction ne retourne rien mais modifie la matrice
    """
    if matrice == None:
        raise ("Objet matrice nul")

    matrice[2][ligne][colonne] = valeur


def get_ligne(mat, lig):
    lignes = get_nb_lignes(mat)
    if lignes < lig:
        return None

    colonnes = get_nb_colonnes(mat)
    ligne_demandee = []
    for j in range(colonnes):
        ligne_demandee.append(get_valeur(mat, lig, j))

    return ligne_demandee

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
    valeur_ejectee = get_valeur(matrice, num_ligne, 0)
    set_valeur(matrice, num_ligne, 0, nouvelle_valeur)
    for j in range(1, get_nb_colonnes(matrice)-1):
        set_valeur(matrice, num_ligne, j, get_valeur(matrice, num_ligne, j+1))

    return valeur_ejectee
    

def decalage_ligne_a_droite(matrice, num_ligne, nouvelle_valeur=0):
    """
    decale la ligne num_ligne d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne

    :param matrice: la matrice considérée
    :param num_ligne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    valeur_ejectee = get_valeur(matrice, num_ligne, get_nb_colonnes(matrice)-1)
    set_valeur(matrice, num_ligne, get_nb_colonnes(matrice)-1, nouvelle_valeur)
    for j in range(get_nb_colonnes(matrice)-1, 0, -1):
        set_valeur(matrice, num_ligne, j, get_valeur(matrice, num_ligne, j-1))

    return valeur_ejectee


def decalage_colonne_en_haut(matrice, num_colonne, nouvelle_valeur=0):
    """
    decale la colonne num_colonne d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne

    :param matrice: la matrice considérée
    :param num_colonne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    valeur_ejectee = get_valeur(matrice, 0, num_colonne)
    set_valeur(matrice, 0, num_colonne, nouvelle_valeur)
    for i in range(1, get_nb_lignes(matrice)-1):
        set_valeur(matrice, i, num_colonne, get_valeur(matrice, i+1, num_colonne))

    return valeur_ejectee

def decalage_colonne_en_bas(matrice, num_colonne, nouvelle_valeur=0):
    """
    decale la colonne num_colonne d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne

    :param matrice: la matrice considérée
    :param num_colonne: le numéro de la ligne à décaler
    :param nouvelle_valeur: la valeur à placer
    :return: la valeur qui a été ejectée lors du décalage
    """
    valeur_ejectee = get_valeur(matrice, get_nb_lignes(matrice)-1, num_colonne)
    set_valeur(matrice, get_nb_lignes(matrice)-1, num_colonne, nouvelle_valeur)
    for i in range(get_nb_lignes(matrice)-1, 0, -1):
        set_valeur(matrice, i, num_colonne, get_valeur(matrice, i-1, num_colonne))

    return valeur_ejectee
