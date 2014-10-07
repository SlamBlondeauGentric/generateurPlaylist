#!/usr/bin/python3

import argparse
import logging
import sys
from locale import str
from argparse import Namespace

logging.basicConfig(filename='mon_fichier_log', level=logging.DEBUG)

'''Arguments positionnels'''
parser = argparse.ArgumentParser()
'''Duree_playlist est la duree de la playlist en minutes'''
parser.add_argument("duree_playlist", help="duree de la playlist en minutes", type=int)

'''Type_playlsit est le format de sortie de la playlist'''
parser.add_argument("type_playlist", help="Format de sortie de la playlist", choices=["m3u","xspf","pls"])

'''Nom_playlist est le nom de la playlist'''
parser.add_argument("nom_playlist", help="Nom du fichier de la playlist")


'''Arguments optionnels'''
'''--g permettera de specifie un genre de musique '''
parser.add_argument("--g", action='append', help="genre de musique voulue '", nargs=2)

'''--ar permettre de specifie un artiste voulue'''
parser.add_argument("--ar", action='append', help="artiste voulu ", nargs=2)

'''--alb permettera de specifie un album voulue'''
parser.add_argument("--alb",action='append', help="album voulue", nargs=2)

'''--t permettera de specifie un titre voulue'''
parser.add_argument("--t", action='append', help="titre voulue", nargs=2)

'''--marge c'est la marge supplementaire a ajouter a la duree'''
parser.add_argument("--marge", help="marge supplementaire a ajoute a la duree", type=int)

'''--sg permettera de specifie un sous genre'''
parser.add_argument("--sg", action='append', help="sous genre possible")

'''--r permettera de rentre une recherche'''
parser.add_argument("--r", help="recherche d'un titre selon une expression")

args = parser.parse_args()

'''Fonction qui permet de verifier si l'utilisateur a bien saisie un entier pour une quantite voulue'''
def VerifInt (quantity):
    
        try:
            goodQte=int(quantity)
            logging.info("Un entier a bien ete saisie.")
            
            if goodQte >=0 and goodQte<=100:
                logging.info("L'entier saisie est bien positif et inferieur a 100.")   
                return goodQte
            elif (goodQte<0 and goodQte>=-100):
                    '''On convertie le negatif en positif'''
                    goodQte=abs(goodQte)
                    logging.info("L'entier saisie est negatif saisie a ete transformer en entier positif.") 
                    return goodQte
            else:
                    logging.error("L'entier saisie est inferieur a -100 ou superieur a 100.")
                    exit(2)
        except ValueError:
            logging.error("Erreur de conversion,la saisie est une chaine.")
            print("Il y a une erreur, veuillez saisir un entier naturel.")
            exit(1)

	
'''Fonction qui permet la verification de tout les quantites de chaque arguments saisies'''  
def Veriff ():
	
    '''Liste des arguments du programme'''
    Attributs=['g','ar','sg','alb','t','r']
        
    ''''Boucle pour parcourir la liste des arguments saisies par l'utilisateur'''
    for arg in Attributs:
        
        '''On initialise un compteur d'argument par option'''
        i=0
        '''On initialise le pourcentage total de la playlist'''
        pourcentage=0      
        if getattr(args, arg) is not None:
            ListeArg=getattr(args, arg)
            logging.info("L'option "+arg+" est bien present.")
            
            '''Tant qu'il y a plusieurs argument de la meme option'''
            while i<len(ListeArg):
                Argument=ListeArg[i]
                ArgumentEntier=Argument[1]
          
                '''On incremente le curseur'''
                i=i+1
            
                try:
                    '''On va donner l'entier saisie a une fonction pour la verifier'''
                    argVerif=VerifInt(ArgumentEntier)
                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")
                    
                try:
                    '''On rentre la saisie dans une variable qui totalise les pourcentages saisies'''
                    pourcentage+=argVerif
        
                    '''On verifie le le total des pourcentages saisies par l'utilisateur.'''
                    if pourcentage>100:
                        print("Votre demande est superieur a 100%, veuillez saisir un valeur dont le total ne depasse pas ce seuil!")
                        
                        logging.info("Le programme c'est arrete car le max de pourcentage a ete atteint.")
                        exit(3)
                except Exception:
                    logging.error("Le compte des pourcentages c'est mal effectue.")
            
                try:
                    '''On remplace la saisir de l'utilisateur par un entier'''    
                    setattr(args,arg,argVerif)
                except Exception:
                    logging.error("Le remplacement de la valeur entier n'a pas pu se faire.")
                    exit(4)
        else:
            logging.info("L'option "+arg+" n'est pas presente.")

'''On execute la requete qui va lancer le controle des saisies (argument et entier) de l'utilisateur'''
Veriff()











