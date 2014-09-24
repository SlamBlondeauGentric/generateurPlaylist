import argparse
from locale import str

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
parser.add_argument("--g", help="genre de musique voulue '", type=str)

'''--ar permettre de specifie un artiste voulue'''
parser.add_argument("--ar", help="artiste voulu ", type=str)

'''--alb permettera de specifie un album voulue'''
parser.add_argument("--alb", help="album voulue", type=str)

'''--t permettera de specifie un titre voulue'''
parser.add_argument("--t", help="titre voulue", type=str)

'''--marge c'est la marge supplementaire a ajouter a la duree'''
parser.add_argument("--marge", help="marge supplementaire a ajoute a la duree", type=int)

'''--sg permettera de specifie un sous genre'''
parser.add_argument("--sg", help="sous genre possible", type=str, action="store_true")

args = parser.parse_args()
if args.

print("Duree: "+str(args.duree_playlist)+" minutes")
print("Format: "+args.type_playlist)
print("Nom du fichier: "+args.nom_playlist)

