# -*- coding: utf-8 -*-
"""
                           Projet Splaby'O
        Projet Python 2020-2021 de 1ere année et AS DUT Informatique Orléans

"""
import random

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
liste_cartes = ['╬', '╦', '╣', '╗', '╩', '═', '╝', 'Ø', '╠', '╔', '║', 'Ø', '╚', 'Ø', 'Ø', 'Ø']


def Carte(nord, est, sud, ouest, objet=0):
    """
    permet de créer une carte

    :param nord: un booléen indiquant s'il y a un mur ou non au nord
    :param est: un booléen indiquant s'il y a un mur ou non à l'est
    :param sud: un booléen indiquant s'il y a un mur ou non au sud
    :param ouest: un booléen indiquant s'il y a un mur ou non à l'ouest
    :param objet: un entier positif indiquant si la carte possède un objet (0 indique l'absence d'objet)
    :return: la structure que vous avez choisie pour représenter les cartes avec comme couleur "aucune"
    """
    ...

def est_valide(carte):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zero, un ou deux murs

    :param carte: une carte
    :return: un booléen indiquant si la carte est valide ou non
    """
    ...


def mur_nord(carte):
    """
    retourne un booléen indiquant si la carte possède un mur au nord

    :param carte: une carte
    :return: True si il y a un mur au nord
    """
    ...


def mur_sud(carte):
    """
    retourne un booléen indiquant si la carte possède un mur au sud

    :param carte: une carte
    :return: True si il y a un mur au sud
    """
    return carte["sud"]


def mur_est(carte):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est

    :param carte: une carte
    :return: True si il y a un mur à l'est
    """
    return carte["est"]


def mur_ouest(carte):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest

    :param carte: une carte
    :return: True si il y a un mur à l'ouest
    """
    return carte["ouest"]


def get_liste_joueurs(carte):
    """
    retourne la liste des joueurs se trouvant sur la carte

    :param carte: une carte
    :return: une liste de joueurs
    """
    return carte["pions"]


def set_liste_joueurs(carte, liste_joueurs):
    """
    place la liste des joueurs passées en paramètre sur la carte

    :param carte: une carte
    :param liste_joueurs: la liste des joueurs à placer
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    ...


def possede_joueur(carte, joueur):
    """
    retourne un booléen indiquant si la carte possède le joueur passé en paramètre

    :param carte: une carte
    :param joueur: un joueur
    :return: True si le joueur est sur la carte False sinon
    """
    ...


def get_objet(carte):
    """
    retourne la valeur de l'objet qui se trouve sur la carte (0 si pas d'objet)

    :param carte: une carte
    :return: un entier positif
    """
    ...


def poser_objet(carte, objet):
    """
    pose l'objet passé en paramètre sur la carte

    :param carte: une carte
    :param objet: un entier positif (0 pour ne mettre aucun objet
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    ...


def prendre_objet(carte):
    """
    enlève le objet qui se trouve sur la carte

    :param carte: une carte
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    ...


def set_couleur(carte, couleur):
    """
    change le couleur d'une carte

    :param carte: une carte
    :param couleur: une couleur
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    ...


def get_couleur(carte):
    """
    retourne la couleur d'une carte

    :param carte: une carte
    :return: retourne la couleur de la carte
    """
    ...


def prendre_joueur(carte, joueur):
    """
    enlève le joueur passé en paramètre de la carte. Si le joueur n'y était pas ne fait rien

    :param carte: une carte
    :param joueur: un joueur
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    ...


def poser_joueur(carte, joueur):
    """
    pose le joueur passé en paramètre sur la carte. Si le joueur y était déjà ne fait rien

    :param carte: une carte
    :param joueur: le joueur à poser
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    ...


def tourner_horaire(carte):
    """
    fait tourner la carte dans le sens horaire

    :param carte: une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    ...

    
def tourner_antihoraire(carte):
    """
    fait tourner la carte dans le sens anti-horaire

    :param carte: une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    ...

    
def tourner_aleatoire(carte):
    """
    fait tourner la carte d'un nombre de tours aléatoire

    :param carte: une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    ...


def coder_murs(carte):
    """
    code les murs sous la forme d'un entier dont le codage binaire
    est de la forme bNbEbSbO où bN, bE, bS et bO valent
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier

    :param carte: une carte
    :return: un entier indice du caractère semi-graphique de la carte
    """
    ...


def decoder_murs(carte, code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment

    :param carte: une carte
    :param code: un entier codant les murs d'une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    ...


def to_char(carte):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)

    :param carte: une carte
    :return: un caractère semi graphique
    """
    ...


def passage_nord(carte1, carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    ...


def passage_sud(carte1, carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    ...


def passage_ouest(carte1, carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    ...


def passage_est(carte1, carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    ...
