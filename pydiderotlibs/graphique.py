# -*- coding: utf-8 -*-
#

# import des librairies
import sys
import math
import pygame


from time import sleep  # pour rendre transparent côté élève l'utilisation de "sleep"
from random import randint #pour la fonction vecteur2

from .couleurs import rgb


def creer_fenetre(largeur=200, hauteur=300, orientation_axe_ordonnees=False, titre="Fenetre graphique"):
    fenetre(largeur, hauteur, orientation_axe_ordonnees , titre)


def window(largeur=600, hauteur=500, orientation_axe_ordonnees=False, titre="Fenetre graphique"):
    fenetre(largeur, hauteur, orientation_axe_ordonnees , titre)


def fenetre(largeur=600, hauteur=500, orientation_axe_ordonnees=False, titre="Fenetre graphique"):
    """
    Crée et affiche une fenêtre graphique.
    Alias: ``windows()``, ``creer_fenetre()``
    Arguments:
        largeur (int, optionel): Largeur de la fenetre en pixels (``600`` par défaut)
        hauteur (int, optionel): Hauteur de la fenetre en pixels (``500`` par défaut)
        orientation_axe_ordonnees: Si on met cet argument à True, l'axe des ordonnées sera orienté de bas en haut comme en maths. Sinon il est orienté dans l'autre sens comme habituellement en informatique (``False`` par défaut) 
        titre (str, optionel): Titre de la fenetre (``Fenetre graphique`` par défaut)
    """

    pygame.init()
    global fenetre
    global axeMath
    axeMath = orientation_axe_ordonnees
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre)
    # active la répétition des touches
    pygame.key.set_repeat(1)
    fenetre.fill(rgb('blanc'))
    pygame.display.update()

def ordo(y):
    global axeMath
    ymax = pygame.display.Info().current_h
    if axeMath :
        return ymax-y
    else :
        return y

def ecoute_evenements():
    demande_evenements()


def events():
    demande_evenements()


def demande_evenements():
    """
    Récupère les évenements pygame gère la fermeture de la fenetre et retourne les évenements formatés.

    Renvoie un dictionnaire d'évenements formaté comme suit:
    ``{'touche1': None, 'touche2':None, 'souris': [x,y], 'click': [x,y]}``

    Les valeurs ``None`` pour les touches peuvent surprendre mais il est nécéssaire d'utiliser un dictionnaire pour avoir les coordonnées
    éventuelles de la souris lors d'un click par exemple. Pour les touches clavier, l'importance est la présence de la cléf et la valeur associée est donc ``None``.

    - Les caractères alphanumériques sont encodés en ascii (``'a'``, ``'n'``, ``';'``) et, si présent, leur valeur est ``None``.
    - les touches spéciales ont les clefs ``'espace'``, ``'haut'``, ``'bas'``, ``'droite'``, ``'gauche'`` et, si présent, leur valeur est ``None``.
    - Un clic avec le bouton gauche de la souris ajoute une clef ``'clic'``. Sa valeur est une liste ``[x, y]`` des coordonnées de la souris.
    - Un déplacement de la souris ajoute une clef ``'souris'``. Sa valeur est une liste ``[x, y]`` des coordonnées de la souris.

    Alias: ``events()``, ``ecoute_evenements()``

    """

    # Initialisation du dictionnaire de sortie
    evenements = {}

    touches_speciales = {
        'haut': pygame.K_UP,
        'bas': pygame.K_DOWN,
        'gauche': pygame.K_LEFT,
        'droite': pygame.K_RIGHT,
        'espace': pygame.K_SPACE
    }

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for c, v in touches_speciales.items():
                # On parcourt le dictionnaire par clef, valeur
                # Par exmple c = 'haut' et v = pygame.K_UP
                if event.key == v:
                    # L'important est simplement d'avoir la clef dans le dictionnaire.
                    # La valeur n'a pas d'importance et est donc None
                    evenements[c] = None

            # Si l'unicode peut être convertit en ascii, on ajoute la clef au
            # dictionnaire sous unicode
            if event.unicode.encode('ascii', 'ignore'):
                evenements[event.unicode] = None

        # Gestion des evenements souris
        elif event.type == pygame.MOUSEMOTION:
            evenements['souris'] = list(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            evenements['clic'] = list(event.pos)

    return evenements


def efface(couleur='blanc'):
    """Efface l'écran.
    Arguments:
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur de remplissage de l'écran (``'blanc'`` par défaut).
    """
    fenetre.fill(rgb(couleur))
    pygame.display.update()


def erase(couleur='blanc'):
    efface(couleur)


def trace_cercle(x, y, couleur='bleu', rayon=50, epaisseur=0):
    cercle(x, y, couleur, rayon, epaisseur)


def circle(x, y, couleur='bleu', rayon=50, epaisseur=0):
    cercle(x, y, couleur, rayon, epaisseur)


def cercle(x, y, couleur='bleu', rayon=25, epaisseur=0):
    """
    Trace un cercle dans la fenetre graphique.

    Alias: ``circle()``, ``trace_cercle()``

    Arguments:
        x (int): Abscisse du centre du cercle
        y (int): Ordonnée du centre du cercle
        rayon (int, optionel): Rayon du cercle (25 par défaut)
        epaisseur (int, optionel): Epaisseur du cercle (``0`` par défaut). Si ``0``, le cercle sera rempli et apparaitra comme un disque.
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du cercle (bleu par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.circle(fenetre, couleur, (x, ordo(y)), rayon, epaisseur)
    pygame.display.update()


def trace_point(x, y, couleur='bleu'):
    point(x, y, couleur)


def point(x, y, couleur='bleu'):
    """
    Trace un point dans la fenetre graphique.

    Alias: ``trace_point()``

    Arguments:
        x (int): Abscisse du point
        y (int): Ordonnée du point
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du point (bleu par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.circle(fenetre, couleur, (x, ordo(y)), 1, 0)
    pygame.display.update()


def trace_rectangle(x, y, largeur, hauteur, couleur='bleu', epaisseur=0):
    rectangle(x, y, largeur, hauteur, couleur, epaisseur)


def rectangle(x, y, largeur, hauteur, couleur='bleu', epaisseur=0):
    """
    Trace un rectangle horizontal dans la fenetre graphique .

    Le sommet haut-gauche à pour coordonnées ``(x,y)``, la ``largeur`` est la taille en abscisse
    et la ``hauteur`` la taille en ordonnée.

    Alias: ``trace_rectangle()``

    Arguments:
        x (int): abscisse du sommet haut gauche du rectangle
        y (int): ordonnée du sommet haut gauche du rectangle
        largeur (int): taille du rectangle sur l'axe des abscisses
        hauteur (int): taille du rectangle sur l'axe des ordonnées
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du rectangle (``bleu`` par défaut)
        epaisseur (int, optionnel): Epaisseur des cotés du rectangle (``0`` par défaut). Si ``0``, le rectangle est rempli.

    """
    couleur = rgb(couleur)
    pygame.draw.rect(fenetre, couleur, (x, ordo(y), largeur, hauteur), epaisseur)
    pygame.display.update()


def trace_triangle(x1, y1, x2, y2, x3, y3, couleur='bleu', epaisseur=0):
    triangle(x1, y1, x2, y2, x3, y3, couleur, epaisseur)


def triangle(x1, y1, x2, y2, x3, y3, couleur='bleu', epaisseur=0):
    """
    Trace un triangle dans la fenetre graphique .

    Alias: ``trace_triangle()``

    Arguments:
        x1 (int): abscisse du premier sommet du triangle
        y1 (int): ordonnée du premier sommet du triangle
        x2 (int): abscisse du deuxième sommet du triangle
        y2 (int): ordonnée du deuxième sommet du triangle
        x3 (int): abscisse du troisième sommet du triangle
        y3 (int): ordonnée du troisième sommet du triangle
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du triangle (``bleu`` par défaut)
        epaisseur (int, optionnel): Epaisseur des cotés du triangle (``0`` par défaut). Si ``0``, le triangle est rempli.

    """
    couleur = rgb(couleur)
    pygame.draw.polygon(fenetre, couleur, [(x1, ordo(y1)), (x2, ordo(y2)), (x3, ordo(y3))], epaisseur)
    pygame.display.update()


def trace_segment(x1, y1, x2, y2, couleur='bleu', epaisseur=2):
    segment(x1, y1, x2, y2, couleur, epaisseur)


def segment(x1, y1, x2, y2, couleur='bleu', epaisseur=2):
    """
    Trace un segment entre les points de coordonées ``(x1, y1)`` et ``(x2, y2)``.

    Alias: ``trace_segment()``

    Arguments:
        x1 (int): abscisse de la première extremité du segment
        y1 (int): ordonnée de la première extremité du segment
        x2 (int): abscisse de la deuxieme extrémité du segment
        y2 (int): ordonnée de la deuxieme extrémité du segment
        couleur (:ref:`couleur <couleur>`, optionel): Couleur du segment (``bleu`` par défaut)
        epaisseur (int, optionel): Epaisseur du segment (``2`` par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.lines(fenetre, couleur, False, [(x1, ordo(y1)), (x2, ordo(y2))], epaisseur)
    pygame.display.update()


def trace_vecteur(x, y, v, couleur='rouge', epaisseur=2):
    vecteur(x, y, v, couleur, epaisseur)


def vector(x, y, v, couleur='rouge', epaisseur=2):
    vecteur(x, y, v, couleur, epaisseur)


def vecteur(x, y, v, couleur='rouge', epaisseur=2):
    """
    Trace la représentation du vecteur ``v`` à partir du point d'origine ``(x, y)``.

    Alias: ``vector()``, ``trace_vecteur()``

    Arguments:
        x (int): abscisse du point d'origine de la représentation du vecteur
        y (int): ordonnée du point d'origine de la représentation du vecteur
        v (list): Coordonnées de la deuxieme extrémité du segment
        couleur (:ref:`couleur <couleur>`, optionel): Couleur du segment (``rouge`` par défaut)
        epaisseur (int, optionel): Epaisseur du segment (``2`` par défaut)
    """

    couleur = rgb(couleur)

    trace_segment(x, y, x + v[0], y + v[1], couleur, epaisseur)
    w1 = [0, 0]
    w2 = [0, 0]
    w1[0] = -.3 * math.cos(15 * math.pi / 180) * v[0] + .3 * math.sin(15 * math.pi / 180) * (-v[1])
    w1[1] = -.3 * math.cos(15 * math.pi / 180) * v[1] + .3 * math.sin(15 * math.pi / 180) * v[0]
    w2[0] = -.3 * math.cos(15 * math.pi / 180) * v[0] - .3 * math.sin(15 * math.pi / 180) * (-v[1])
    w2[1] = -.3 * math.cos(15 * math.pi / 180) * v[1] - .3 * math.sin(15 * math.pi / 180) * v[0]
    pygame.draw.polygon(
        fenetre,
        couleur,
        [
            (x + v[0], ordo(y + v[1])),
            (x + v[0] + w1[0], ordo(y + v[1] + w1[1])),
            (x + v[0] + w2[0], ordo(y + v[1] + w2[1])),
            (x + v[0], ordo(y + v[1]))
        ],
        0
    )
    pygame.display.update()

def vecteur2(xv,yv, couleur='rouge', epaisseur=2):
    """
    Trace la représentation du vecteur de coordonnées ``(xv, yv)`` à partir d'une origine choisie au hasard.

    Alias: ``vector2()``, ``trace_vecteur2()``

    Arguments:
        xv (int): abscisse du vecteur
        yv (int): ordonnée du vecteur
        couleur (:ref:`couleur <couleur>`, optionel): Couleur du segment (``rouge`` par défaut)
        epaisseur (int, optionel): Epaisseur du segment (``2`` par défaut)
    """

    ymax = pygame.display.Info().current_h
    xmax = pygame.display.Info().current_w
    x = randint(xv, xmax - xv)
    y = randint(yv , ymax - yv)
    v = [xv,yv]
    vector(x,y,v,couleur,epaisseur)


def trace_vecteur2(xv,yv, couleur='rouge', epaisseur=2):
    vecteur2(xv,yv, couleur, epaisseur)


def vector2(xv,yv, couleur='rouge', epaisseur=2):
    vecteur2(xv,yv, couleur, epaisseur)


def trace_image(x, y, nom, largeur=100, hauteur=100):
    image(x, y, nom, largeur, hauteur)


def image(x, y, nom, largeur=100, hauteur=100):
    """
    Trace une image dans la fenetre graphique.

    Alias:``trace_image()``

    Arguments:
        x (int): Abscisse du centre de l'image
        y (int): Ordonnée du centre de l'image
        nom (str) : nom du fichier image (qui doit être dans le répertoire du script)
        largeur (int, optionel): Largeur de l'image (100 par défaut)
        hauteur (int, optionel): Hauteur de l'image (100 par défaut)
    """
    pygame_image = pygame.transform.scale(pygame.image.load(
        nom).convert_alpha(), (largeur, hauteur))
    fenetre.blit(pygame_image, (int(x - largeur / 2), ordo(int(y - hauteur / 2))))
    pygame.display.update()


def trace_explosion(x, y, couleur='orange', r=50, c=0.5, n=10):
    explosion(x, y, couleur, r, c, n)


def explosion(x, y, couleur='orange', r=25, c=0.5, n=10):
    '''
    Trace un polygône régulier étoilé à ``2n`` côté,
    de rayon extérieur ``r``,
    et tel que le rayon intérieur est égal à ``c*r``
    (pour ``c=0``, le polygône est réduit à ``n`` rayons du cencle de rayon ``r``
    pour ``c=1``, c'est un polygône régulier à ``2n`` côtés)

    Alias: ``trace_explosion()``

    Arguments:
        x (int): Abscisse du centre de l'explosion
        y (int): Ordonnée du centre de l'explosion
        couleur (:ref:`couleur <couleur>`, optionel): Couleur (``orange`` par défaut)
        r (int): Rayon extérieur
        c (float):Coefficient pour obtenir le rayon intérieur égal à ``c*r``
        n (int): Nombre de sommets
    '''
    couleur = rgb(couleur)
    pointlist = []
    theta = 2 * math.pi / n
    for k in range(n):
        pointlist.append((
            x + r * math.cos(k * theta),
            ordo(y + r * math.sin(k * theta))
        ))
        pointlist.append((
            x + c * r * math.cos((k + 1 / 2) * theta),
            ordo(y + c * r * math.sin((k + 1 / 2) * theta))
        ))
    pointlist.append((x + r, ordo(y)))
    pygame.draw.polygon(fenetre, couleur, pointlist)
    pygame.display.update()


def trace_axes(color='noir'):
    axes(color)


def axes(color='noir'):
    '''
    Dessine les axes de coordonnées pour une meilleure compréhension par les élèves.

    Alias: ``trace_axes()``
    '''
    couleur = rgb(color)
    ymax = pygame.display.Info().current_h
    xmax = pygame.display.Info().current_w
    epaisseur = 2
    correction = 0
    if axeMath:
        ## cette correction vient du fait que les textes continuent d'être définis par rapport à leur coin haut-gauche même si l'axe est à l'envers
        correction = 12
    pygame.draw.lines(fenetre, couleur, False, [(5, ordo(0)), (5, ordo(ymax))], epaisseur)
    pygame.draw.lines(
        fenetre, couleur, False, [
            (0, ordo(ymax - 5)), (5, ordo(ymax))], epaisseur)
    pygame.draw.lines(
        fenetre, couleur, False, [
            (10, ordo(ymax - 5)), (5, ordo(ymax))], epaisseur)
    pygame.draw.lines(fenetre, couleur, False, [(0, ordo(5)), (xmax, ordo(5))], epaisseur)
    pygame.draw.lines(
        fenetre, couleur, False, [
            (xmax - 5, ordo(0)), (xmax, ordo(5))], epaisseur)
    pygame.draw.lines(
        fenetre, couleur, False, [
            (xmax - 5, ordo(10)), (xmax, ordo(5))], epaisseur)
    font = pygame.font.Font(None, 24, bold=False, italic=False)
    text = font.render(str(ymax), 1, couleur)
    fenetre.blit(text, (15, ordo(ymax - 35 + correction)))
    text = font.render("y", 1, couleur)
    fenetre.blit(text, (15, ordo(ymax - 17 + correction)))
    text = font.render(str(xmax), 1, couleur)
    fenetre.blit(text, (xmax - 35, ordo(10 + correction)))
    text = font.render("x", 1, couleur)
    fenetre.blit(text, (xmax - 15, ordo(25 + correction)))
    text = font.render("0", 1, couleur)
    fenetre.blit(text, (10, ordo(10 + correction)))
    pygame.display.update()

