# -*- coding: utf-8 -*-
"""
                           Projet Splaby'O
        Projet Python 2020-2021 de 1ere année et AS DUT Informatique Orléans

"""
from joueur import *


def Participants(noms_joueurs, liste_couleurs, humain=True):
    """
    crée une liste de participants dont les noms sont dans la liste de noms passés en paramètre.
    Les joueurs sont numéroté de 1 à N dans l'ordre de leur création
    Par défaut tous les joueurs sont des ordinateurs sauf le joueur 1 en fonction du paramètre humain
    Attention! il ne s'agit pas d'une simple liste de joueurs mais il faudra des informations permettant
    de gérer la notion de joueur courant, de tour de jeu (une fois que tous les joueurs ont joué)

    :param noms_joueurs: une liste de chaines de caractères
    :param liste_couleurs: la liste des couleurs choisis pour chaque joueur
    :param humain: un booléen indiquant si le joueur 1 est humain ou non
    :return: la structure que vous avez choisie pour représenter les participants
    """
    ...

def ajouter_joueur(participants, joueur):
    """
    ajoute un nouveau joueur

    :param participants: les participants actuels
    :param joueur: le joueur à ajouter
    :return: cette fonction ne retourne rien mais modifie la liste des participants
    """
    ...

    
def init_aleatoire_premier_joueur(participants):
    """
    tire au sort le premier joueur courant

    :param participants: les participants
    :return: la fonction ne retourne rien mais modifie la liste des participants
    """
    ...


def get_num_joueur_courant(participants):
    """
    retourne le numéro du joueur courant

    :param participants: les participants
    :return: un nombre entre 1 et 4 indiquant le numéro du joueur courant
    """
    ...


def get_num_premier_joueur(participants):
    """
    return le numéro du joueur qui a joué en premier

    :param participants: les participants
    :return: un nombre entre 1 et 4 indiquant le numéro du joueur qui a joué en premier
    """
    ...


def init_premier_joueur(participants, num_joueur):
    """
    initialialise le premier joueur courant au joueur qui porte le numéro num_joueur

    :param participants: les participants
    :param num_joueur: un nombre entre 1 et 4
    :return: rien cette fonction modifie la liste des participants
    """
    ...


def set_joueur_courant(participants, num_joueur):
    """
    force le joueur courant au joueur qui porte le numéro num_joueur

    :param participants: les participants
    :param num_joueur: un nombre entre 1 et 4
    :return: rien cette fonction modifie la liste des participants
    """
    ...


def changer_joueur_courant(participants):
    """
    passe au joueur suivant (change le joueur courant donc)

    :param participants: les participants
    :return: cette fonction modifie la liste des participants et
             retourne un booléen indiquant si on est revenu au joueur qui a commencé la partie
    """
    ...


def get_nb_joueurs(participants):
    """
    retourne le nombre de joueurs participant à la partie

    :param participants: les participants
    :return: le nombre de joueurs de la partie
    """
    ...


def get_joueur_par_num(participants, num_joueur):
    """
    retourne le joueur de numéro num_joueur

    :param participants: les participants
    :param num_joueur: le numéro du joueur souhaité
    :return: le joueur qui porte le numéro indiqué
    """
    ...


def get_joueur_par_nom(participants, nom_joueur):
    """
    retourne le joueur de numéro num_joueur

    :param participants: les participants
    :param nom_joueur: le nom du joueur souhaité
    :return: le joueur qui porte le nom indiqué, None si aucun joueur ne porte ce nom
    """
    ...


def get_joueur_courant(participants):
    """
    retourne le joueur courant

    :param participants: les participants
    :return: cette fonction ne retourne rien mais modifie la liste des participants
    """
    ...


def mise_a_jour_surface(participants, couverture):
    """
    permet de mettre à jour la surface couverte par chaque joueur

    :param participants: les participants
    :param couverture: un dictionnaire qui indique pour chaque couleur le nombre de cases de cette couleur
    :return: cette fonction ne retourne rien mais modifie la liste des participants
    """
    ...

    
def classement_joueurs(participants):
    """
    Retourne une liste de participants triée suivant les critètres 1) la surface couverte 2) la réserve d'encre

    :param participants: les participants
    :return: une liste de joueurs triée dans l'ordre décroissant
    """
    ...
