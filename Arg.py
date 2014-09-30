import argparse
import logging
from locale import str

'''Arguments positionnels'''
from argparse import Namespace
parser = argparse.ArgumentParser()
'''Duree_playlist est la duree de la playlist en minutes'''
parser.add_argument("duree_playlist", help="duree de la playlist en minutes", type=int)

'''Type_playlsit est le format de sortie de la playlist'''
parser.add_argument("type_playlist", help="Format de sortie de la playlist", choices=["m3u","xspf","pls"])

'''Nom_playlist est le nom de la playlist'''
parser.add_argument("nom_playlist", help="Nom du fichier de la playlist")

'''print("Duree: "+str(args.duree_playlist)+" minutes")
print("Format: "+args.type_playlist)
print("Nom du fichier: "+args.nom_playlist)'''

'''Arguments optionnels'''
'''--g permettera de specifie un genre de musique '''
parser.add_argument("--g", help="genre de musique voulue '", nargs=2)

'''--ar permettre de specifie un artiste voulue'''
parser.add_argument("--ar", help="artiste voulu ", nargs=2)

'''--alb permettera de specifie un album voulue'''
parser.add_argument("--alb", help="album voulue", nargs=2)

'''--t permettera de specifie un titre voulue'''
parser.add_argument("--t", help="titre voulue", nargs=2)

'''--marge c'est la marge supplementaire a ajouter a la duree'''
parser.add_argument("--marge", help="marge supplementaire a ajoute a la duree", type=int)

'''--sg permettera de specifie un sous genre'''
parser.add_argument("--sg", help="sous genre possible")

args = parser.parse_args()

'''Fonction qui permet de verifier si l'utilisateur a bien saisie un entier pour une quantite voulue'''
def VerifInt (quantity):
    if quantity >0:
        try:
            return int(quantity)
        except ValueError:
            print("Erreur de conversion")

	
'''Fonction qui permet la verification de tout les quantites de chaque arguments saisies'''  
def Veriff ():
	
    Attributs=('g','ar','sg','alb','t')
    pourcentage=0
    for arg in Attributs:
        Argu=getattr(args, arg)
        if Argu is not None:
            argVerif=VerifInt(Argu[1])
            setattr(args,arg,argVerif)
            pourcentage+=argVerif
    print(pourcentage)
		
Veriff()










