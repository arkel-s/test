""" Projet Vasarely du MOOC FUN
    Auteur Nicolas Clerc
    Date 05/04/2020
    Dessiner un tableau d'art optique d'un pavage hexagonal tricolore avec déformation"""

# importation des bibliotheques turtle et math
import turtle
import math

#PARTIE 1:
# Programme qui dessine un cube
def hexagone(point, longueur, col, centre, rayon): # point(tuple des coordonnées); col (3 couleurs hexagone ); centre (centre de la sphere de déformation); rayon(de la sphere de déformation)
    turtle.speed(0)  # vitesse d'excution du dessin: vitesse lente
    turtle.up()
    x = point[0]  # coordonnes d'origine du premier cube: cela correspond au coin inferieur gauche et coin supérieur droit
    y = point[1]  # de la fenetre du dessin
    turtle.goto(x, y)  # deplacement de la tortue au point d'origine du dessin
    turtle.down()


# ETAPE 2 programmer la fonction de déformation
from math import pi, sin, cos, sqrt, acos, asin, atan2

def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon**2 > zc**2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)                  # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2)           # rayon de la partie émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                 # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r               # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return (xprim, yprim, zprim)

if __name__ == "__main__": # code de test
    for i in range(-150,150,50):
        for j in range(-150,150,50):
            print(deformation((i,j,0), (0,0,100), 100))
        print()

# dessiner les 3 faces de l'hexagone
    # dessin de la première face du cube (la rouge)
    turtle.color(col[1])  # couleur de la face supérieure rouge
    turtle.begin_fill()
    x = x + longueur * (math.cos(0))  # abscisse avant deformation
    y = y + longueur * (math.sin(0))  # ordonnée avant deformation
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)  # coordonnées apres deformation ICI PAS SUR DES COORDONNEES
    turtle.goto(pprim[0], pprim[1])  # la tortue va au point déformé

    x = x + longueur * (math.cos(-1 * math.pi / 3))
    y = y + longueur * (math.sin(-1 * math.pi / 3))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-1 * math.pi))
    y = y + longueur * (math.sin(-1 * math.pi))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-120 * math.pi / 180))
    y = y + longueur * (math.sin(120 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])
    turtle.end_fill()

    # dessin de la deuxième face du cube (bleue)
    turtle.color(col[2])
    turtle.begin_fill()
    x = x + longueur * (math.cos(-60 * math.pi / 180))
    y = y + longueur * (math.sin(-60 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-120 * math.pi / 180))
    y = y + longueur * (math.sin(-120 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-240 * math.pi / 180))
    y = y + longueur * (math.sin(-240 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(60 * math.pi / 180))
    y = y + longueur * (math.sin(60 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])
    turtle.end_fill()

    # dessin de la troisieme face du cube (noire)
    turtle.color(col[3])
    turtle.down()
    turtle.begin_fill()
    x = x + longueur * (math.cos(0 * math.pi / 180))
    y = y + longueur * (math.sin(0 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-120 * math.pi / 180))
    y = y + longueur * (math.sin(-120 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(-180 * math.pi / 180))
    y = y + longueur * (math.sin(-180 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])

    x = x + longueur * (math.cos(60 * math.pi / 180))
    y = y + longueur * (math.sin(60 * math.pi / 180))
    p = (x, y, 0)
    pprim = deformation(p, centre, rayon)
    turtle.goto(pprim[0], pprim[1])
    turtle.end_fill()

# ETAPE 3:
# dessine un pavage de cubes
def pavage (inf_gauche, sup_droit, longueur, col, centre, rayon):
    n = 1  # compteur de ligne de polygones
    angle = math.pi / 3  #
    sup_droit1 = sup_droit  # nouvelle position en hauteur  du polygone apres chaque ligne
    pas = 3 * longueur  # espacement entre deux polygones
    new_inf_gauche = int(inf_gauche - longueur * (1 + math.cos(angle)))  # position de depart  du polygone pour les lignes  paires
    new_sup_droit = int(sup_droit + longueur * (1 + math.cos(angle)))  # position de finale  du polygone pour les lignes  paires

    while sup_droit1 > inf_gauche:  # tant le polygone n'est pas arrivé a la dernière ligne  de la fenêtre
        if n % 2 != 0:  # cas d'une ligne impaire
            for x in range(inf_gauche, sup_droit, pas):
                coordonnees = (x, sup_droit1)
                print(coordonnees)
                hexagone(coordonnees, longueur, col, centre, rayon)
            n += 1
        else:  # cas d'une ligne paire
            for x in range(new_inf_gauche, new_sup_droit, pas):
                coordonnees = (x, sup_droit1)
                hexagone(coordonnees, longueur, col, centre, rayon)
            n += 1
        sup_droit1 = sup_droit1 - longueur * math.sin(angle)

# ETAPE 4: code principal aevc paramètres demandés à l'utilisateur
pavage (inf_gauche, sup_droit, longueur, col, centre, r) # r = rayon de la sphère de déformation
inf_gauche = int(input("Valeurs coordonnées bord inférieur gauche fenêtre de visualisation : "))
sup_droit= int(input("Valeurs coordonnées bord supérieur droit fenêtre de visualisation : "))
longueur = int(input("longueur segment de pavé avant déformation : "))
col1 = int(input("nom de la couleur 1 blue : "))
col2 = int(input("nom de la couleur 2 black: "))
col2 = int(input("nom de la couleur 2 black: "))
centre = int(input(X0, Y0, Z0)) # coordonnées du centre de la sphère de déformante
r = int(input("rayon de la sphère de déformation : "))
turtle.getcanvas().postscript(file="pavage.eps") # enregistrer l'image du pavage dans le fichier "pavage.eps"
turtle.done()

# GAEL, pour les données à rentrer, voir le mail que j'ai envoyé

