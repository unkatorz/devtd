#!/usr/bin/env python3
# coding: utf-8

import csv
import os
from sys import argv
import re 

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def total_list(m: int, n: int,liste, chemin: str) -> float:
    """
    Fonction principale pour traiter la ligne d'entrée.
    
        Parameters:
            line (str): Une ligne contenant M, N, une liste de mots, et un chemin de fichier.
        
        Returns:
            float: La somme des produits des valeurs ou "BAD INPUT" en cas d'erreur.
    """
    
    try:
        total_sum = 0
        column = []
        for element in liste:
            column.append(element)
            print(element)
        with open(chemin, mode='r') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=1):
                if m <= i <= n:
                    price = float(row['price'])
                    quantity = float(row['quantity'])
                    
                    total_sum += price * quantity
                
        return total_sum
            

    
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
    
    #    Déclaration des variables

    parameter_list = line.split(" ")
    m = int(parameter_list[0])+1
    n = int(parameter_list[1])+1
    liste_word = parameter_list[2:-1]
    chemin = parameter_list[len(parameter_list)-1]

    if m > n : raise BadInputException()

    for element in liste_word:
        if not re.match(r"^[a-zA-Z]+$", element): raise BadInputException()

    if chemin[-4:] != ".csv": raise BadInputException()

    with open(chemin, "r") as file:
        content = csv.reader(file, delimiter=',')
        for row in content:
            if not len(row) > 1: raise BadInputException()

    try:
        result = total_list(m,n,liste_word,chemin)
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
