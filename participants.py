# -*- coding: utf-8 -*-
"""
                           Projet Splaby'O
        Projet Python 2020-2021 de 1ere année et AS DUT Informatique Orléans

"""
from joueur import *
from random import randint

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
    tour = 0
    participants = [tour]
    nombre_joueurs = len(noms_joueurs)
    for indice_joueur in range(nombre_joueurs):
        nom_joueur = noms_joueurs[indice_joueur]
        couleur_joueur = liste_couleurs[indice_joueur]
        joueur = Joueur(nom_joueur, couleur_joueur, type_joueur=('H' if (indice_joueur == 0 and humain) else 'O'))

        participants.append(joueur)

    return participants

def ajouter_joueur(participants, joueur):
    """
    ajoute un nouveau joueur

    :param participants: les participants actuels
    :param joueur: le joueur à ajouter
    :return: cette fonction ne retourne rien mais modifie la liste des participants
    """
    participants.append(joueur)
    
def init_aleatoire_premier_joueur(participants):
    """
    tire au sort le premier joueur courant

    :param participants: les participants
    :return: la fonction ne retourne rien mais modifie la liste des participants
    """
    effectif = get_nb_joueurs(participants)
    indice_alea = randint(1, effectif)
    participants[indice_alea]['joueur_courant'] = True
    participants[indice_alea]["premier_joueur"] = True


def get_num_joueur_courant(participants):
    """
    retourne le numéro du joueur courant

    :param participants: les participants
    :return: un nombre entre 1 et 4 indiquant le numéro du joueur courant
    """
    num_joueur_courant = 1
    taille_participants = get_nb_joueurs(participants)
    print(participants)
    if taille_participants > 1:
        for indice_joueur in range(1, taille_participants):
            joueur = participants[indice_joueur]
            if joueur['joueur_courant']:
                return indice_joueur #indice -> numéro

    return num_joueur_courant



def get_num_premier_joueur(participants):
    """
    return le numéro du joueur qui a joué en premier

    :param participants: les participants
    :return: un nombre entre 1 et 4 indiquant le numéro du joueur qui a joué en premier
    """
    indice_joueur_courant = 1
    if get_nb_joueurs(participants) > 1:
        taille_participants = get_nb_joueurs(participants)
        for i in range(1, taille_participants):
            joueur = participants[i]
            if joueur['premier_joueur']:
                return i


    return indice_joueur_courant


def init_premier_joueur(participants, num_joueur):
    """
    initialialise le premier joueur courant au joueur qui porte le numéro num_joueur

    :param participants: les participants
    :param num_joueur: un nombre entre 1 et 4
    :return: rien cette fonction modifie la liste des participants
    """
    if len(participants) > 1 and num_joueur > 0:
        #participants[num_joueur]['joueur_courant'] = True
        participants[num_joueur]['premier_joueur'] = True


def set_joueur_courant(participants, num_joueur):
    """
    force le joueur courant au joueur qui porte le numéro num_joueur

    :param participants: les participants
    :param num_joueur: un nombre entre 1 et 4
    :return: rien cette fonction modifie la liste des participants
    """
    #print("num_joueur=", num_joueur)
    #print("len(participants)=", len(participants))
    #print_participants(participants)
    if len(participants) > 1 and num_joueur > 0:
        participants[num_joueur]['joueur_courant'] = True
        get_joueur_courant(participants)['joueur_courant'] = False


def changer_joueur_courant(participants):
    """
    passe au joueur suivant (change le joueur courant donc)

    :param participants: les participants
    :return: cette fonction modifie la liste des participants et
             retourne un booléen indiquant si on est revenu au joueur qui a commencé la partie
    """
    effectif = get_nb_joueurs(participants)
    num_joueur_courant = get_num_joueur_courant(participants)
    num_nv_joueur = None
    if num_joueur_courant == effectif: #s'il s'agit du joueur qui a le dernier numéro
        num_nv_joueur = 1
    else:
        num_nv_joueur = num_joueur_courant+1

    if participants[num_nv_joueur]['premier_joueur']:
        incr_tour(participants)


    participants[num_joueur_courant]['joueur_courant'] = False
    participants[num_nv_joueur]['joueur_courant'] = True
    return participants[num_nv_joueur]['premier_joueur']


def get_tour(participants):
    return participants[0]

def incr_tour(participants):
    participants[0] += 1


def get_nb_joueurs(participants):
    """
    retourne le nombre de joueurs participant à la partie

    :param participants: les participants
    :return: le nombre de joueurs de la partie
    """
    return len(participants)-1


def get_joueur_par_num(participants, num_joueur):
    """
    retourne le joueur de numéro num_joueur

    :param participants: les participants
    :param num_joueur: le numéro du joueur souhaité
    :return: le joueur qui porte le numéro indiqué
    """
    return participants[num_joueur]


def get_joueur_par_nom(participants, nom_joueur):
    """
    retourne le joueur de numéro num_joueur

    :param participants: les participants
    :param nom_joueur: le nom du joueur souhaité
    :return: le joueur qui porte le nom indiqué, None si aucun joueur ne porte ce nom
    """
    for num_joueur in range(1, len(participants)):
        joueur = get_joueur_par_num(participants, num_joueur)
        if joueur['nom'] == nom_joueur:
            return joueur

    return None


def get_joueur_courant(participants):
    """
    retourne le joueur courant

    :param participants: les participants
    :return: cette fonction ne retourne rien mais modifie la liste des participants
    """
    return get_joueur_par_num(participants, get_num_joueur_courant(participants))


def mise_a_jour_surface(participants, couverture):
    """
    permet de mettre à jour la surface couverte par chaque joueur

    :param participants: les participants
    :param couverture: un dictionnaire qui indique pour chaque couleur le nombre de cases de cette couleur
    :return: cette fonction ne retourne rien mais modifie la liste des participants
    """
    for num_joueur in range(1, len(participants)):
        joueur = get_joueur_par_num(participants, num_joueur)
        couleur_joueur = joueur['couleur']
        nbr_cases_couleur = couverture[couleur_joueur]
        joueur['surface'] = nbr_cases_couleur


def classement_joueurs(participants):
    """
    Retourne une liste de participants triée suivant les critètres 1) la surface couverte 2) la réserve d'encre

    :param participants: les participants
    :return: une liste de joueurs triée dans l'ordre décroissant
    """

    classement = None
    participants_purgeable = participants.copy()
    if len(participants) > 2:
        classement = []
        while len(participants_purgeable) > 2:
            meilleur_joueur = participants_purgeable[1]
            num_meilleur_joueur = 1
            #utilisation de la fonction de comparaison de joueur.py
            for num_joueur in range(1, len(participants)-len(classement)):
                if comparer(meilleur_joueur, participants_purgeable[num_joueur]) == -1 or comparer(meilleur_joueur, participants_purgeable[num_joueur]) == 0:
                    meilleur_joueur = participants_purgeable[num_joueur]
                    num_meilleur_joueur = num_joueur

            classement.append(meilleur_joueur)
            participants_purgeable.pop(num_meilleur_joueur)

        return classement.reverse()

    return classement
    #perte de l'indice lors d'un tri, utilisation d'un dic recommandé
