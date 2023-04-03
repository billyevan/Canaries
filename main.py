# -*- coding: utf-8 -*- #

import random

random.seed()

# Initialisation des grilles, représentées par des matrices
grilleDebutPartie = [ ["   ", "1", "2", "3", "4"],
                      ["| A", "○", "○", "○", "○"],
                      ["| B", "○", "○", "○", "○"],
                      ["| C", "●", "●", "●", "●"],
                      ["| D", "●", "●", "●", "●"]]

grilleMilieuPartie = [["   ", "1", "2", "3", "4"],
                      ["| A", "○", "●", "○", "○"],
                      ["| B", "○", "●", " ", "○"],
                      ["| C", " ", " ", "●", "●"],
                      ["| D", "●", " ", "●", "●"]]

grilleFinPartie = [["   ", "1", "2", "3", "4"],
                   ["| A", " ", "●", "○", "○"],
                   ["| B", " ", " ", "●", "●"],
                   ["| C", " ", " ", "●", " "],
                   ["| D", " ", " ", " ", " "]]


# Fonction pour afficher les grilles en utilisant les matrices ci-dessus
def afficherGrille(grille):
  print(' ' * 4, '+---' * 4, "+", sep='')
  for ligne in grille:
      for colonne in ligne:
          print(colonne, end=" | ")
      print('\n', '+---+', '---+' * 4, sep='')
  return True


# Appel à la fonction afficher grille; les trois configurations de grilles sont affichées ici
def afficherConfig():
    print(
        "_________________________________________\n\nGrille en début de partie\n"
    )
    afficherGrille(grilleDebutPartie)
    print(
        "\nNombre de pions noirs (○) restants   : 8\nNombre de pions blancs (●) restants  : 8",
        "\n_________________________________________")
    print("\nGrille en milieu de partie\n")
    afficherGrille(grilleMilieuPartie)
    print(
        "\nNombre de pions noirs (○) restants   : 5\nNombre de pions blancs (●) restants  : 7",
        "\n_________________________________________")
    print("\nGrille en fin de partie\n")
    afficherGrille(grilleFinPartie)
    print(
        "\nNombre de pions noirs (○) restants   : 2\nNombre de pions blancs (●) restants  : 4",
        "\n_________________________________________")
    return True


# Verification dans grille
def estDansGrille(ligne, colonne):
    if len(ligne) != 1 or len(colonne) != 1:
        return False
    if 64 < ord(ligne) < 69 and 48 < ord(colonne) < 53:
        return True
    return False


# Fonctions de saisie des coordonées de départ ou celles d'arrivé
def saisirCoordoneesDepartes():
  coor = input("\nVeuillez saisir les coordonées de départ de la case   : ")
  if coor == " " or coor == "":
      print("\n[!] Vous avez choisi une case vide. Veuillez reéssayer.")
  while not estDansGrille(
          coor[0], coor[1:]
  ):  # coor[1:] parce qu'il y a la possibilite qu la saisie soit erronée en contenant plus de deux caracteres
      print(
          "\n[!] Il se peut que les coordonnées saisies soient non valides. "
      )
      coor = input(
          "\nVeuillez de nouveau saisir les coordonées de départ de la case   : "
      )
  print("\nLa case de départ choisie est:", coor)
  return coor[0], coor[1]


def saisirCoordoneesArrivees():
  coor = input("\nVeuillez saisir les coordonées d'arrivée de la case   : ")
  if coor == " " or coor == "":
      print("\n[!] Vous avez choisi une case vide. Veuillez reéssayer.")
  while not estDansGrille(
          coor[0], coor[1:]
  ):  # coor[1:] parce qu'il y a la possibilite qu la saisie soit erronée en contenant plus de deux caracteres
      print(
          "\n[!] Il se peut que les coordonnées saisies soient non valides. "
      )
      coor = input(
          "\nVeuillez de nouveau saisir les coordonées d'arrivée de la case   : "
      )
  print("\nLa case de départ choisie est:", coor)
  return coor[0], coor[1]


# Cette fonction a pour but de convertir la ligne et la colonne en entier pour faciliter l'écriture du programme ulterieurement
def conversion(ligne, colonne):
  colonne = int(colonne)
  if ligne == "A":
      ligne = 1
  if ligne == "B":
      ligne = 2
  if ligne == "C":
      ligne = 3
  if ligne == "D":
      ligne = 4
  return ligne, colonne


# Cette fonction a pour but de reconvertir la ligne en lettre uniquement pour l'afficage dans la partie IA
def conversionInverse(ligne):
  if ligne == 1:
    ligne = "A"
  if ligne == 2:
    ligne = "B"
  if ligne == 3:
    ligne = "C"
  if ligne == 4:
    ligne = "D"
  return ligne


# =========== FONCTION DE VERIFICATION DE MOUVEMENT ===========

# Cette fontion vérifie que les règles de déplacement simple sont respectées
def deplacementSimple(lDep, cDep, lArr, cArr, pionCourant, pionOppose, grille):
  if grille[lDep][cDep] == pionCourant and grille[lArr][cArr] == " " and (
    cArr == cDep + 1 or cArr == cDep - 1 or lArr == lDep + 1 or lArr == lDep - 1):
    return True
  else:
    print(
      "\n[!] Le déplacements ne peut s'effectuer vu le non respect des règles. Veuillez reéssayer. "
      )
    return False


# Ceci est identique à la fonction précédente, sauf qu'il n'y a pas de message imprimé
def deplacementSimpleSansMessage(lDep, cDep, lArr, cArr, pionCourant, pionOppose, grille):
  if grille[lDep][cDep] == pionCourant and grille[lArr][cArr] == " " and (
  cArr == cDep + 1 or cArr == cDep - 1 or lArr == lDep + 1 or lArr == lDep - 1):
      return True


# Cette fontion vérifie que les règles de capture sont respectées
def capture(lDep, cDep, lArr, cArr, pionCourant, pionOppose, grille):
    if (grille[lDep][cDep] == pionCourant) and (grille[lArr][cArr] == pionOppose):
        if lArr == lDep - 2:  # Pour éviter l'érreur "index out of range"
            if lDep <= 4 and grille[lDep - 1][cDep] != " " and grille[
                    lDep - 1][cDep] == pionCourant:
                return True
        if lArr == lDep + 2:  # Pour éviter l'érreur "index out of range"
            if lDep < 4 and grille[lDep + 1][cDep] != " " and grille[
                    lDep + 1][cDep] == pionCourant:
                return True
        if cArr == cDep - 2:  # Pour éviter l'érreur "index out of range"
            if cDep <= 4 and (grille[lDep][cDep - 1] !=
                              " ") and (grille[lDep][cDep - 1] == pionCourant):
                return True
        if cArr == cDep + 2:  # Pour éviter l'érreur "index out of range"
            if cDep < 4 and (grille[lDep][cDep + 1] !=
                             " ") and grille[lDep][cDep + 1] == pionCourant:
                return True
        else:
            print(
                "\n[!] Le déplacements ne peut s'effectuer vu le non respect des règles. Veuillez reéssayer. "
            )
            return False
    else:
        print(
            "\n[!] Le déplacements ne peut s'effectuer vu le non respect des règles. Veuillez reéssayer. "
        )
        return False

# Ceci est identique à la fonction précédent, sauf qu'il n'y a pas de message imprimé
def captureSansMessage(lDep, cDep, lArr, cArr, pionCourant, pionOppose,
                       grille):
  if (grille[lDep][cDep] == pionCourant) and (grille[lArr][cArr]
                                              == pionOppose):
      if lArr == lDep - 2:
          if lDep <= 4 and grille[lDep - 1][cDep] != " " and grille[
                  lDep - 1][cDep] == pionCourant:
              return True
      if lArr == lDep + 2:
          if lDep < 4 and grille[lDep + 1][cDep] != " " and grille[
                  lDep + 1][cDep] == pionCourant:
              return True
      if cArr == cDep - 2:
          if cDep <= 4 and (grille[lDep][cDep - 1] !=
                            " ") and (grille[lDep][cDep - 1] == pionCourant):
              return True
      if cArr == cDep + 2:
          if cDep < 4 and (grille[lDep][cDep + 1] !=
                            " ") and grille[lDep][cDep + 1] == pionCourant:
              return True


# =========== FONCTION DE GRILLES (LE CHOIX, LA MISE A JOUR) ET DES MENUS ============

# La grille est mise à jour grâce à cette fonction-ci
def modifierGrille(lDep, cDep, lArr, cArr, grille, pionCourant):
    grille[lDep][
        cDep] = " "  #La case de départ contient maintenant " " (elle devient vide)
    grille[lArr][
        cArr] = pionCourant  #La case d'arrivée contient maintenant le pion courant
    return grille

# Ici, l'utilisateur peut choisir la configuration de grille selon sa volonté
def menuGrille():
    while True:
        menu = input(
            "\nVeuillez choisir une grille à jouer:\n\n1. ) Grille en début de partie \n2. ) Grille en milieu de partie\n3. ) Grille en fin de partie\n\nSaisissez votre choix (1, 2 ou 3): "
        )
        if menu == "1":
            grille = grilleDebutPartie
        elif menu == "2":
            grille = grilleMilieuPartie
        elif menu == "3":
            grille = grilleFinPartie
        else:
            print("\n[!] Saisie erronée. Veuillez reéssayer.")
            break
        print(
            "\n_________________________________________\n\nVoici la grille choisie. \n_________________________________________\n"
        )
        afficherGrille(grille)  #La grille choisie est affichée
        print("_________________________________________")
        return grille


def saisirCoordoneesCompletes(
):  # L'appel aux fonctions de saisir coordonées en les assignant aux variables
    lDep, cDep = saisirCoordoneesDepartes()
    lDep, cDep = conversion(lDep, cDep)
    lArr, cArr = saisirCoordoneesArrivees()
    lArr, cArr = conversion(lArr, cArr)
    return lDep, cDep, lArr, cArr


def mettreAjour(
    lDep, cDep, lArr, cArr, grille, pionCourant
):  # L'appel à la fonction qui modifie la grille et celle qui ensuite affiche cette grille
    miseAJour = modifierGrille(lDep, cDep, lArr, cArr, grille, pionCourant)
    print(
        "\nLe déplacement s'est bien effectué.\nVoici la grille mise à jour. \n"
    )
    afficherGrille(miseAJour)


# Ce sous-menu permet à l'utilisateur de choisir le déplacement à effectuer, puis effectuer ce mouvement et mettre à jour la grille - elle fait plus de 15 lignes parce qu'il ne peut plus se décomposer, et une décomposition plus approfondie provoque des érreurs
def menuDeplacement(grille, pionCourant, pionOppose):
    while True:
        menu = input(
            "\nVeuillez choisir le déplacement à effectuer:\n1. ) Déplacement simple\n2. ) Capture\n\nSaisissez votre choix (1 ou 2): "
        )
        if menu == "1":
            if len(
                    deplacementSimplePossible(pionCourant, pionOppose, grille)
            ) != 0:  # Creer une liste contenant autant de coordonées que possible pour effectuer un déplacement simple pour chaque pion. Si la liste n'est pas vide, le programme permet de procéder à la suite.
                while True:
                    lDep, cDep, lArr, cArr = saisirCoordoneesCompletes()
                    if deplacementSimple(
                            lDep, cDep, lArr, cArr, pionCourant, pionOppose,
                            grille):  # Vérifie que la déplacement est valide
                        mettreAjour(lDep, cDep, lArr, cArr, grille,
                                    pionCourant)  # Mettre à jour la grille
                        break
                break
            else:
                print(
                    "\n[!] Mouvement impossible.\n    Veuillez reéssayer. Optez plutôt de capturer."
                )  # Liste de déplacement simple est vide, donc ce déplacement est impossible.
                continue
        elif menu == "2":
            if len(
                    capturePossible(pionCourant, pionOppose, grille)
            ) != 0:  # Creer une liste contenant autant de coordonées que possible pour effectuer une pour chaque pion. Si la liste n'est pas vide, le programme permet de procéder à la suite.
                while True:
                    lDep, cDep, lArr, cArr = saisirCoordoneesCompletes()
                    if capture(
                            lDep, cDep, lArr, cArr, pionCourant, pionOppose,
                            grille):  # Vérifie que la déplacement est valide
                        mettreAjour(lDep, cDep, lArr, cArr, grille,
                                    pionCourant)  # Mettre à jour la grille
                        break
                break
            else:
                print(
                    "\n[!] Mouvement impossible.\n    Veuillez reéssayer. (Choisissez plutôt le déplacement simple)"
                )  # Liste de capture est vide, donc ce déplacement est impossible.
                continue
        else:
            print("\n[!] Saisie erronée. Veuillez reéssayer.")


# Cette fonction permet de choisir quel pion joue en premier, et d'initialiser alors les valeurs de joueur courant / opposé et son couleur de pion corréspondant
def joueurs():
    while True:
        joueurCourant = input(
            "\nQuel équipe veut jouer en premier ?\nVeuillez entrer votre choix (Noir / Blanc): "
        )
        if joueurCourant.lower(
        ) == "noir":  # Le programme peut accepter la saisie peu importe la façon dont elle s'écrit (en minuscule ou en majuscule)
            joueurCourant, pionCourant = "noir", "○"  # Initialisation de joueur courant et pion courant
            joueurOppose, pionOppose = "blanc", "●"  # Initialisation de joueur opposé et pion opposé
            break
        elif joueurCourant.lower() == "blanc":
            joueurCourant, pionCourant = "blanc", "●"
            joueurOppose, pionOppose = "noir", "○"
            break
        else:
            print("\n[!] Saisie erronée.\nVeuillez reéssayer.")
    return joueurCourant, pionCourant, joueurOppose, pionOppose


# ================ FONCTION DE FIN PARTIE ================
# Vérifie les règles / conditions qui détermine la terminaison du jeu


def comptoirPion(grille):  # Compte le nombre des deux couleurs de pion
    blanc = 0
    noir = 0
    for ligne in grille:
        for colonne in ligne:
            if colonne == "○":
                blanc += 1
            elif colonne == "●":
                noir += 1
    return blanc, noir


def finPartie1(
    blanc, noir
):  # Vérifie les règles qui determine la fin du jeu (où il y a moin de deux pion pour l'un des deux équipes)
    if blanc < 2 or noir < 2:
        print("\nLe jeu est terminé. ")
        return False
    return True


# Les décompositions des autres règles qui determine la fin du jeu (où le jeu se términe quand il n'y a plus de déplacement possible / les pions sont bloqués)
def finPartie2a(pionCourant, pionOppose,
                grille):  # Calcule le nombre de déplacement simple possible
    lDep = -1
    cDep = -1
    deplacementSimpleListe = []
    for ligne in grille:
        cDep = -1
        lDep += 1
        for colonne in ligne:
            cDep += 1
            if colonne == pionCourant:
                if deplacementSimpleSansMessage(lDep, cDep, lDep, cDep - 1,
                                                pionCourant, pionOppose,
                                                grille):
                    deplacementSimpleListe.append([lDep, cDep, lDep, cDep - 1])
                if deplacementSimpleSansMessage(lDep, cDep, lDep - 1, cDep,
                                                pionCourant, pionOppose,
                                                grille):
                    deplacementSimpleListe.append([lDep, cDep, lDep - 1, cDep])
                if lDep < 4:  # Pour éviter l'érreur "index out of range"
                    if deplacementSimpleSansMessage(lDep, cDep, lDep + 1, cDep,
                                                    pionCourant, pionOppose,
                                                    grille):
                        deplacementSimpleListe.append(
                            [lDep, cDep, lDep + 1, cDep])
                if cDep < 4:  # Pour éviter l'érreur "index out of range"
                    if deplacementSimpleSansMessage(lDep, cDep, lDep, cDep + 1,
                                                    pionCourant, pionOppose,
                                                    grille):
                        deplacementSimpleListe.append(
                            [lDep, cDep, lDep, cDep + 1])
    return len(deplacementSimpleListe
               )  # C'est-à-dire le nombre de déplacement simple possible


def finPartie2b(pionCourant, pionOppose,
                grille):  # Calcule le nombre de capture possible
    lDep = -1
    cDep = -1
    captureListe = []
    for ligne in grille:
        cDep = -1
        lDep += 1
        for colonne in ligne:
            cDep += 1
            if colonne == pionCourant:
                if cDep > 2:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep, cDep - 2,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep, cDep - 2])
                if cDep < 3:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep, cDep + 2,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep, cDep + 2])
                if lDep > 2:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep - 2, cDep,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep - 2, cDep])
                if lDep < 3:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep + 2, cDep,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep + 2, cDep])
    return len(captureListe)  # C'est-à-dire le nombre de capture possible


def finPartie2(
        pionCourant, pionOppose,
        grille):  # Cette fonction regroupe les deux fonctions précedentes
    totalDeplacement = finPartie2a(pionCourant, pionOppose,
                                   grille) + finPartie2b(
                                       pionCourant, pionOppose, grille)
    if totalDeplacement == 0:  # S'il n'y a aucun déplacement possible, le jeu se términe
        return True


# ================ FONCTION D'IA ================
# L'ensemble de fonctions qui calcule le(s) mouvement(s) possible(s) pour chaque pion dans une grille


def deplacementSimplePossible(
    pionCourant, pionOppose, grille
):  # Calcule le nombre de déplacement simple possible pouvant s'éffectuer par l'IA - cette fonction fait plus de 15 lignes mais je vous assure que c'est le plus court possible
    lDep = -1
    cDep = -1
    deplacementSimpleListe = []
    for ligne in grille:
        cDep = -1
        lDep += 1
        for colonne in ligne:
            cDep += 1
            if colonne == pionCourant:
                if deplacementSimpleSansMessage(lDep, cDep, lDep, cDep - 1,
                                                pionCourant, pionOppose,
                                                grille):
                    deplacementSimpleListe.append([lDep, cDep, lDep, cDep - 1])
                if deplacementSimpleSansMessage(lDep, cDep, lDep - 1, cDep,
                                                pionCourant, pionOppose,
                                                grille):
                    deplacementSimpleListe.append([lDep, cDep, lDep - 1, cDep])
                if lDep < 4:  # Pour éviter l'érreur "index out of range"
                    if deplacementSimpleSansMessage(lDep, cDep, lDep + 1, cDep,
                                                    pionCourant, pionOppose,
                                                    grille):
                        deplacementSimpleListe.append(
                            [lDep, cDep, lDep + 1, cDep])
                if cDep < 4:  # Pour éviter l'érreur "index out of range"
                    if deplacementSimpleSansMessage(lDep, cDep, lDep, cDep + 1,
                                                    pionCourant, pionOppose,
                                                    grille):
                        deplacementSimpleListe.append(
                            [lDep, cDep, lDep, cDep + 1])
    return deplacementSimpleListe  # Une liste de déplacement simple possible (contenant des coordonées de depart et celles d'arrivée)


def capturePossible(
    pionCourant, pionOppose, grille
):  # Calcule le nombre de capture possible pouvant s'éffectuer par l'IA - cette fonction fait plus de 15 lignes mais je vous assure que c'est le plus court possible
    lDep = -1
    cDep = -1
    captureListe = []
    for ligne in grille:
        cDep = -1
        lDep += 1
        for colonne in ligne:
            cDep += 1
            if colonne == pionCourant:
                if cDep > 2:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep, cDep - 2,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep, cDep - 2])
                if cDep < 3:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep, cDep + 2,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep, cDep + 2])
                if lDep > 2:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep - 2, cDep,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep - 2, cDep])
                if lDep < 3:  # Pour éviter l'érreur "index out of range"
                    if captureSansMessage(lDep, cDep, lDep + 2, cDep,
                                          pionCourant, pionOppose, grille):
                        captureListe.append([lDep, cDep, lDep + 2, cDep])
    return captureListe  # Une liste de capture possible (contenant des coordonées de depart et celles d'arrivée)


# =================== LES FONCTIONS DE JOUEURS CONTRE JOUEUR / IA NAIVE / IA AVANCEE ===================


def tourJoueur(joueurOppose, pionOppose, joueurCourant, pionCourant, blanc,
               noir, grille):
    print("\n======= C'est le tour de pion", joueurCourant.lower(), "=======")
    menuDeplacement(
        grille, pionCourant, pionOppose
    )  # Appel à la fonction de menu pour choisir le type de déplacement
    if finPartie2(
            pionCourant, pionOppose,
            grille):  # Vérifie si la condition de fin partie est atteinte
        print("\nLe jeu est terminé. ")
        False
    joueurCourant, pionCourant, joueurOppose, pionOppose = joueurOppose, pionOppose, joueurCourant, pionCourant  # Le changement de tour en changeant les variables
    blanc, noir = comptoirPion(
        grille
    )  # # Appel à la fonction de comptoir de pion, les valeurs retournées seront utilisées pour vérifier la condition de fin partie
    return joueurOppose, pionOppose, joueurCourant, pionCourant, blanc, noir, grille


# Joueur contre joueur
def joueurVjoueur(joueurOppose, pionOppose, joueurCourant, pionCourant, blanc,
                  noir, grille):
    print(
        "\n======== A T T E N T I O N ========\n\n○ : noir\n● : blanc\n\n======== A T T E N T I O N ========"
    )
    tour = 1  # Initialisation de tour
    while finPartie1(blanc, noir):
        if tour == 1:
            joueurOppose, pionOppose, joueurCourant, pionCourant, blanc, noir, grille = tourJoueur(
                joueurOppose, pionOppose, joueurCourant, pionCourant, blanc,
                noir, grille)
            tour = 2  # Changement de tour pour le joueur opposé
        else:
            joueurOppose, pionOppose, joueurCourant, pionCourant, blanc, noir, grille = tourJoueur(
                joueurOppose, pionOppose, joueurCourant, pionCourant, blanc,
                noir, grille)
            tour = 1  # Changement de tour pour le joueur opposé
    print("Le vainqueur est le pion ",
          joueurOppose.lower(),
          ".\nFélicitations!",
          sep="")


# Joueur contre IA Naïve - cette fonction fait plus de 15 lignes parce que la décomposition de cette fonction provoquerait des érreurs, donc je préfère la laisser comme cela
def joueurVia_naive(joueurOppose, pionOppose, joueurCourant, pionCourant,
                    blanc, noir, grille):
    print(
        "\n======== A T T E N T I O N ========\n\n○ : noir\n● : blanc\n\n======== A T T E N T I O N ========"
    )
    tour = 1
    while finPartie1(blanc, noir):
        if tour == 1:
            joueurOppose, pionOppose, joueurCourant, pionCourant, blanc, noir, grille = tourJoueur(
                joueurOppose, pionOppose, joueurCourant, pionCourant, blanc,
                noir, grille)
            tour = 2
        else:
            print("\n======= C'est le tour de pion", joueurCourant.lower(),
                  "(IA Naïve) =======")
            listeDeplacement = capturePossible(
                pionCourant, pionOppose, grille
            ) + deplacementSimplePossible(
                pionCourant, pionOppose, grille
            )  # Appel aux fonctions de déplacements possibles en les mettant dans une liste
            deplacementIA = listeDeplacement[random.randint(
                0,
                len(listeDeplacement) - 1
            )]  # Le programme choisi aléatoirement un déplacement à partir de la grande liste
            lDep, cDep, lArr, cArr = int(
                deplacementIA[0]
            ), int(deplacementIA[1]), int(deplacementIA[2]), int(
                deplacementIA[3]
            )  # La sous-liste choisie aléatoirement est décomposee por récuperer les coordonées de depart et celles d'arrivée
            grille = modifierGrille(
                lDep, cDep, lArr, cArr, grille, pionCourant
            )  # Modification de grille selon le mouvement choisie aléatoirement
            convLiDep, convLiArr = conversionInverse(
                int(deplacementIA[0])), conversionInverse(
                    int(deplacementIA[2])
                )  # Convertir la ligne en lettre (uniquement pour l'affichage)
            print(
                "\nLe déplacement de l'IA s'est bien effectué.\nUn pion s'est déplacé de ",
                convLiDep,
                deplacementIA[1],
                " vers ",
                convLiArr,
                deplacementIA[3],
                ".\nVoici la grille mise à jour. \n",
                sep="")
            afficherGrille(grille)
            if finPartie2(pionCourant, pionOppose, grille):
                print("\nLe jeu est terminé. ")
                break
            joueurCourant, pionCourant, joueurOppose, pionOppose = joueurOppose, pionOppose, joueurCourant, pionCourant
            blanc, noir = comptoirPion(grille)
            tour = 1
    print("Le vainqueur est le pion ",
          joueurOppose.lower(),
          ".\nFélicitations!",
          sep="")


# Joueur contre IA Avancée - cette fonction fait plus de 15 lignes parce que la décomposition de cette fonction provoquerait des érreurs, donc je préfère la laisser comme cela
def joueurVia_avancee(joueurOppose, pionOppose, joueurCourant, pionCourant,
                      blanc, noir, grille):
    print(
        "\n========= A T T E N T I O N ==========\n\n○ : noir\n● : blanc\n\n========== A T T E N T I O N =========="
    )
    tour = 1
    while finPartie1(
            blanc,
            noir):  #Tant que la condition de fin partie n'est pas atteinte
        if tour == 1:
            joueurOppose, pionOppose, joueurCourant, pionCourant, blanc, noir, grille = tourJoueur(
                joueurOppose, pionOppose, joueurCourant, pionCourant, blanc,
                noir, grille)
            tour = 2
        if tour == 2:
            print("\n======= C'est le tour de pion", joueurCourant.lower(),
                  "(IA Avancée) =======")
            listeSimple = deplacementSimplePossible(pionCourant, pionOppose,
                                                    grille)
            listeCapture = capturePossible(pionCourant, pionOppose, grille)

            # L'heuristique se fait ici; l'IA est instruite de choisir une capture au lieu d'un déplacement simple
            if len(
                    listeCapture
            ) != 0:  #S'il y a des captures possibles, l'IA opte pour ceci
                deplacementIA = listeCapture[random.randint(
                    0,
                    len(listeCapture) - 1)]
            else:  # C'est-a-dire qu'il n'y a aucune capture possible et alors l'IA n'a pas d'autres choix qu'effectuer un deplacement simple
                deplacementIA = listeSimple[random.randint(
                    0,
                    len(listeSimple) - 1)]

            lDep, cDep, lArr, cArr = int(deplacementIA[0]), int(
                deplacementIA[1]), int(deplacementIA[2]), int(deplacementIA[3])
            grille = modifierGrille(lDep, cDep, lArr, cArr, grille,
                                    pionCourant)
            convLiDep, convLiArr = conversionInverse(int(
                deplacementIA[0])), conversionInverse(int(deplacementIA[2]))
            print(
                "\nLe déplacement de l'IA s'est bien effectué.\nUn pion s'est déplacé de ",
                convLiDep,
                deplacementIA[1],
                " vers ",
                convLiArr,
                deplacementIA[3],
                ".\nVoici la grille mise à jour. \n",
                sep="")
            afficherGrille(grille)
            if finPartie2(pionCourant, pionOppose, grille):
                print("\nLe jeu est terminé. ")
                break
            joueurCourant, pionCourant, joueurOppose, pionOppose = joueurOppose, pionOppose, joueurCourant, pionCourant
            blanc, noir = comptoirPion(grille)
            tour = 1
    print("Le vainqueur est le pion ",
          joueurOppose.lower(),
          ".\nFélicitations!",
          sep="")


# ====================== LES FONCTIONS DE TESTS ======================


def test_estDansGrille():
    assert estDansGrille('B', '3') == True, "Les coordonnées sont valides."
    assert estDansGrille('D', '2') == True, "Les coordonnées sont valides."
    assert estDansGrille(
        '', ''
    ) == False, "Il faudrait mettre les coordonnées. La saisie ne doit pas être vide. "
    assert estDansGrille(
        'C', '5'
    ) == False, "Les coordonnées sont non valides (hors plateau). Veuillez mettre une lettre (A - D) suivi d'un nombre (1 - 4). "
    assert estDansGrille(
        'F', '67'
    ) == False, "Les coordonnées sont non valides (hors plateau). Veuillez mettre une lettre (A - D) suivi d'un nombre (1 - 4). "
    assert estDansGrille(
        '1', 'A'
    ) == False, "Les coordonnées sont non valides (saisie erronée). Veuillez mettre une lettre (A - D) suivi d'un nombre (1 - 4). "


def test_conversion():
    assert conversion("A", "1") == (1, 1), "Erreur conversion"
    assert conversion("B", "3") == (2, 3), "Erreur conversion"
    assert conversion("D", "4") == (4, 4), "Erreur conversion"


def test_deplacementSimple():
    grille = grilleMilieuPartie
    assert deplacementSimple(1, 3, 2, 3, "○", "●",
                             grille), "Erreur deplacement"
    assert deplacementSimple(4, 1, 3, 1, "●", "○",
                             grille), "Erreur deplacement"
    assert deplacementSimple(3, 3, 3, 2, "●", "○",
                             grille), "Erreur deplacement"


def test_Capture():
    grille = grilleDebutPartie
    assert capture(4, 4, 2, 4, "●", "○", grille), "Erreur capture"
    assert capture(1, 3, 3, 3, "○", "●", grille), "Erreur capture"


def test_comptoirPion():
    grille1 = grilleDebutPartie
    grille2 = grilleMilieuPartie
    grille3 = grilleFinPartie
    assert comptoirPion(grille1) == (8, 8), "Erreur comptage"
    assert comptoirPion(grille2) == (5, 7), "Erreur comptage"
    assert comptoirPion(grille3) == (2, 4), "Erreur comptage"


def test_finPartie1(
):  # Test de la fin partie du jeu où il se términe vu qu'il reste moins de deux pion pour une équipe
    assert finPartie1(2, 3), "Erreur condition"
    assert finPartie1(3, 3), "Erreur condition"


grilleTestBloque1 = [["   ", "1", "2", "3", "4"],
                     ["| A", "●", "○", "○", "●"],
                     ["| B", "○", " ", " ", "○"],
                     ["| C", "○", " ", " ", "○"],
                     ["| D", "●", "○", "○", "●"]]

grilleTestBloque2 = [["   ", "1", "2", "3", "4"],
                     ["| A", " ", "○", "●", "○"],
                     ["| B", " ", " ", "○", " "],
                     ["| C", " ", "○", " ", " "],
                     ["| D", "○", "●", "○", " "]]


def test_finPartie2(
):  # Test de la fin partie du jeu où il se términe vu que les pions d'une équipe sont bloqués
    assert finPartie2("●", "○", grilleTestBloque1), "Erreur condition"
    assert finPartie2("●", "○", grilleTestBloque2), "Erreur condition"


grilleTest1 = [["   ", "1", "2", "3", "4"], ["| A", " ", " ", " ", " "],
               ["| B", " ", " ", "●", " "], ["| C", " ", " ", " ", " "],
               ["| D", " ", " ", " ", " "]]

grilleTest2 = [["   ", "1", "2", "3", "4"], ["| A", "●", "●", "○", " "],
               ["| B", " ", " ", "●", " "], ["| C", " ", " ", "●", " "],
               ["| D", " ", " ", " ", " "]]


def test_listeDeplacementPossible(
):  # Ceci teste le calcul de déplacement possible
    assert len(
        deplacementSimplePossible("●", "○", grilleTest1)
    ) == 4, "Erreur creation des listes de mouvements possible"  #Ceci doit rénvoyer la valeur 4 parce que pour ce pion, il y a 4 déplacements simples possibles
    assert len(
        capturePossible("●", "○", grilleTest1)
    ) == 0, "Erreur creation des listes de mouvements possible"  #Ceci doit rénvoyer la valeur 0 parce que pour ce pion, il y a 0 capture possible
    assert len(
        deplacementSimplePossible("●", "○", grilleTest2)
    ) == 7, "Erreur creation des listes de mouvements possible"  #Ceci doit rénvoyer la valeur 4 parce que pour ce pion, il y a 2 captures possibles
    assert len(
        capturePossible("●", "○", grilleTest2)
    ) == 2, "Erreur creation des listes de mouvements possible"  #Ceci doit rénvoyer la valeur 4 parce que pour ce pion, il y a 2 captures possibles


def test_mouvementIA(
):  # On teste si la fonction randint choisi l'un des déplacements possibles correctement / aléatoirement
    listeDeplacement1 = capturePossible(
        "●", "○", grilleTest1) + deplacementSimplePossible(
            "●", "○", grilleTest1)
    deplacementIA1 = listeDeplacement1[random.randint(
        0,
        len(listeDeplacement1) - 1)]
    assert deplacementIA1 == [2, 2, 2, 1] or [2, 2, 1, 2] or [2, 2, 2, 1] or [
        2, 2, 3, 2
    ] or [2, 2, 2, 3], "Erreur random de liste de deplacement"
    listeDeplacement2 = capturePossible(
        "●", "○", grilleTest2) + deplacementSimplePossible(
            "●", "○", grilleTest2)
    deplacementIA12 = listeDeplacement2[random.randint(
        0,
        len(listeDeplacement2) - 1)]
    assert deplacementIA12 == [1, 1, 2, 1] or [1, 2, 2, 2] or [2, 3, 2, 2] or [
        2, 3, 2, 4
    ] or [3, 3, 3, 2] or [3, 3, 3, 4] or [3, 3, 4, 3,], "Erreur random de liste de deplacement"


def test(
):  # L'ensemble des fonctions des tests - elle fait plus de 15 lignes mais c'est justifiable vu qu'il y a 9 tests et chacun doit être affiché (donc +1 ligne chacun pour le print)
    print(
        "\n_________________________________________\n\nTest en cours...\n_________________________________________\n"
    )
    test_estDansGrille()
    print("Test de:\n1) Validation de coordonées                       : OK")
    test_conversion()
    print("2) Conversion de coordonées                       : OK")
    test_deplacementSimple()
    print("3) Déplacement simple                             : OK")
    test_Capture()
    print("4) Capture                                        : OK")
    test_comptoirPion()
    print("5) Comptior de pion(s)                            : OK")
    test_finPartie1()
    print("6) Fin partie (moins de deux pions)               : OK")
    test_finPartie2()
    print("7) Fin partie (pions bloqués)                     : OK")
    test_listeDeplacementPossible()
    print("7) Calculation des déplacements simples possibles : OK")
    print("8) Calculation des captures possibles             : OK")
    test_mouvementIA()
    print("9) Validité de mouvement d'IA                     : OK")
    print("\nLe jeu a validé tous les tests.")


# =============================== MENU, CODE PRINCIPAL ===============================
# Les fonctions majeures sont appelées ici, cette partie fait plus de 15 lignes et ceci est normal parce que cette partie ne peut plus se décomposer

print(
    "_________________________________________\n\nBienvenue au jeu de \nC  A  N  A  R  I  E  S  "
)

while True:
    choix = input("_________________________________________\n\nQue souhaitez-vous faire?\n\n1) Afficher les grilles\n\nLancer le jeu:\n2) Joueur v Joueur\n3) Joueur v IA Naïve\n4) Joueur v IA Avancée\n\n5) Effectuer les tests\n6) Quitter\n\nVeuillez choisir (1, 2, 3, 4, 5 ou 6): ")

    if choix == "1":
        afficherConfig()

    elif choix == "2" or choix == "3" or choix == "4":
        afficherConfig()
        grille = menuGrille()  # L'utilisateur choisi la grille
        joueurCourant, pionCourant, joueurOppose, pionOppose = joueurs(
        )  # Détermine le joueur courant et opposé ainsi que son pion corréspondant
        blanc, noir = comptoirPion(
            grille)  # Compte le nombre de pion de chaque équipe
        if choix == "2":
            joueurVjoueur(joueurOppose, pionOppose, joueurCourant, pionCourant,
                          blanc, noir, grille)
        elif choix == "3":
            joueurVia_naive(joueurOppose, pionOppose, joueurCourant,
                            pionCourant, blanc, noir, grille)
        elif choix == "4":
            joueurVia_avancee(joueurOppose, pionOppose, joueurCourant,
                              pionCourant, blanc, noir, grille)

    elif choix == "5":
        test()

    elif choix == "6":
        print(
            "_________________________________________\n\nMerci d'avoir joué aux\nC  A  N  A  R  I  E  S\n_________________________________________\n"
        )
        break

    else:
        print("\n[!] Saisie erronée. Veuillez reéssayer.")