#!/usr/bin/python3
'''
Created on 14 oct. 2014

@author: kitsune
'''

import sqlalchemy
from Configurations.connexionBDD import loginBDD, mdp
from sqlalchemy import engine

engine = sqlalchemy.create_engine('postgresql://s.blondeau:'+mdp+'@172.16.99.2:5432/radio_libre')



'''metadata = sqlalchemy.MetaData()
morceau = sqlalchemy.Table('morceaux',metadata,Column('titre',str, primary_key = True))'''


