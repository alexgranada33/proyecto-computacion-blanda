# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:56:32 2020

@author: Alex
"""


from textblob.classifiers import NaiveBayesClassifier
with open('sentiment.json','r') as fp:
    cl=NaiveBayesClassifier(fp,format='json')
    
print(cl.classify("estoy ansioso por el examen")) 
print(cl.classify("no me gusta la hambuerguesa"))
print(cl.classify("quiero llorar "))
print(cl.classify("hoy es un hermoso dia"))