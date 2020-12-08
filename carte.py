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
    return {"murs":{"N":nord, "E":est, "S":sud, "O":ouest}, "objet":objet, "joueurs":[], "couleur":None}

def est_valide(carte):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zero, un ou deux murs

    :param carte: une carte
    :return: un booléen indiquant si la carte est valide ou non
    """
    return len([x for x in carte["murs"].values() if x]) <= 2

def mur_nord(carte):
    """
    retourne un booléen indiquant si la carte possède un mur au nord

    :param carte: une carte
    :return: True si il y a un mur au nord
    """
    return carte["murs"]["N"]


def mur_sud(carte):
    """
    retourne un booléen indiquant si la carte possède un mur au sud

    :param carte: une carte
    :return: True si il y a un mur au sud
    """
    return carte["murs"]["S"]


def mur_est(carte):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est

    :param carte: une carte
    :return: True si il y a un mur à l'est
    """
    return carte["murs"]["E"]


def mur_ouest(carte):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest

    :param carte: une carte
    :return: True si il y a un mur à l'ouest
    """
    return carte["murs"]["O"]


def get_liste_joueurs(carte):
    """
    retourne la liste des joueurs se trouvant sur la carte

    :param carte: une carte
    :return: une liste de joueurs
    """
    return carte["joueurs"]


def set_liste_joueurs(carte, liste_joueurs):
    """
    place la liste des joueurs passées en paramètre sur la carte

    :param carte: une carte
    :param liste_joueurs: la liste des joueurs à placer
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    carte["joueurs"] = liste_joueurs


def possede_joueur(carte, joueur):
    """
    retourne un booléen indiquant si la carte possède le joueur passé en paramètre

    :param carte: une carte
    :param joueur: un joueur
    :return: True si le joueur est sur la carte False sinon
    """
    return joueur in carte["joueurs"]


def get_objet(carte):
    """
    retourne la valeur de l'objet qui se trouve sur la carte (0 si pas d'objet)

    :param carte: une carte
    :return: un entier positif
    """
    return carte["objet"]


def poser_objet(carte, objet):
    """
    pose l'objet passé en paramètre sur la carte

    :param carte: une carte
    :param objet: un entier positif (0 pour ne mettre aucun objet
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    carte["objet"] = objet


def prendre_objet(carte):
    """
    enlève le objet qui se trouve sur la carte

    :param carte: une carte
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    carte["objet"] = 0


def set_couleur(carte, couleur):
    """
    change le couleur d'une carte

    :param carte: une carte
    :param couleur: une couleur
    :return: cette fonction ne retourne rien mais modifie la carte
    """
    carte["couleur"] = couleur


def get_couleur(carte):
    """
    retourne la couleur d'une carte

    :param carte: une carte
    :return: retourne la couleur de la carte
    """
    return carte["couleur"]


def prendre_joueur(carte, joueur):
    """
    enlève le joueur passé en paramètre de la carte. Si le joueur n'y était pas ne fait rien

    :param carte: une carte
    :param joueur: un joueur
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    for i in range(len(carte["joueurs"])):
        if carte["joueurs"][i] == joueur:
            carte["joueurs"].pop(i)


def poser_joueur(carte, joueur):
    """
    pose le joueur passé en paramètre sur la carte. Si le joueur y était déjà ne fait rien

    :param carte: une carte
    :param joueur: le joueur à poser
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    if not possede_joueur(carte, joueur):
        carte["joueurs"].append(joueur)

def tourner_horaire(carte):
    """
    fait tourner la carte dans le sens horaire

    :param carte: une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    tmp = carte["murs"]["N"]
    carte["murs"]["N"] = carte["murs"]["O"]
    carte["murs"]["O"] = carte["murs"]["S"]
    carte["murs"]["S"] = carte["murs"]["E"]
    carte["murs"]["E"] = tmp



def tourner_antihoraire(carte):
    """
    fait tourner la carte dans le sens anti-horaire

    :param carte: une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    tmp = carte["murs"]["N"]
    carte["murs"]["N"] = carte["murs"]["E"]
    carte["murs"]["E"] = carte["murs"]["S"]
    carte["murs"]["S"] = carte["murs"]["O"]
    carte["murs"]["O"] = tmp
    
def tourner_aleatoire(carte):
    """
    fait tourner la carte d'un nombre de tours aléatoire

    :param carte: une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    tours = random.randrange(1, 11)
    for _ in range(tours):
        tourner_horaire(carte)



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
    bN = 1 if mur_nord(carte) else 0
    bE = 1 if mur_est(carte) else 0
    bS = 1 if mur_sud(carte) else 0
    bO = 1 if mur_ouest(carte) else 0
    code = bO*2**3 + bS*2**2 + bE*2 + bN
    return code


def decoder_murs(carte, code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment

    :param carte: une carte
    :param code: un entier codant les murs d'une carte
    :return: cette fonction modifie la carte mais ne retourne rien
    """
    bN = code % 2
    bE = (code // 2) % 2
    bS = ((code // 2) // 2) % 2
    bO = (((code // 2) // 2) // 2) % 2

    if bO == 1:
        carte["murs"]["O"] = True
    else:
        if mur_ouest(carte):
            carte["murs"]["O"] = False

    if bS == 1:
        carte["murs"]["S"] = True
    else:
        if mur_sud(carte):
            carte["murs"]["S"] = False

    if bE == 1:
        carte["murs"]["E"] = True
    else:
        if mur_est(carte):
            carte["murs"]["E"] = False

    if bN == 1:
        carte["murs"]["N"] = True
    else:
        if mur_nord(carte):
            carte["murs"]["N"] = False


def to_char(carte):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)

    :param carte: une carte
    :return: un caractère semi graphique
    """
    return liste_cartes[coder_murs(carte)]


def passage_nord(carte1, carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    return not mur_sud(carte2) and not mur_nord(carte1)


def passage_sud(carte1, carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    return not mur_sud(carte1) and not mur_nord(carte2)


def passage_ouest(carte1, carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    return not mur_ouest(carte1) and not mur_est(carte2)


def passage_est(carte1, carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est

    :param carte1: une carte
    :param carte2: une autre carte
    :return: un booléen
    """
    return not mur_est(carte1) and not mur_ouest(carte2)
