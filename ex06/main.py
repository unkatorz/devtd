#!/usr/bin/env python3
# coding: utf-8

import csv
import os
from sys import argv

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def frontal_function(line: str) -> float:
    """
    Fonction principale pour traiter la ligne d'entrée.
    
        Parameters:
            line (str): Une ligne contenant M, N, une liste de mots, et un chemin de fichier.
        
        Returns:
            float: La somme des produits des valeurs ou "BAD INPUT" en cas d'erreur.
    """
    
    try:
        pass

    
    except Exception as e:
        print(f"Exception: {e}")  # Affiche les exceptions pour le débogage
        raise BadInputException("BAD INPUT")

def main(line: str):
    """
    Traite une ligne d'entrée et appelle frontal_function.
    
        Parameters:
            line (str): Une ligne d'entrée.
    
        Returns:
            None: Affiche le résultat ou l'erreur.
    """
    
    #    Définition des variables

    parameter_list = line.split(" ")
    m = parameter_list[0]
    n = parameter_list[1]
    liste_word = parameter_list[2:-1]
    chemin = parameter_list[len(parameter_list)-1]
    
    try:
        
        result = frontal_function()
        print(result)
    except BadInputException:
        print("BAD INPUT")



if __name__ == "__main__":
    
    ### Input file reading
    ### One line = one call to main function
    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                main(line)
            except BadInputException:
                print("BAD INPUT")
    ###
