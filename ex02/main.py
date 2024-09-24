#!/usr/bin/env python3
# coding: utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def sort_name(liste):
    """
    Trie une liste de mots et retourne le premier dans l'ordre alphabétique.
    
    Si deux mots sont identiques, il retourne celui qui apparaît en premier.
    
    Parameters:
    liste (list): Liste de mots à trier.
    
    Returns:
    str: Le premier mot selon l'ordre alphabétique ou d'apparition en cas d'égalité.
    """

    test_liste = sorted(liste)
    return test_liste[0]

def main(line: str):
    """
    Vérifie la validité de l'entrée et affiche le résultat de sort_name.
    
    Parameters:
    line (str): Une chaîne de caractères contenant plusieurs mots séparés par des espaces.
    
    Raises:
    BadInputException: Si l'entrée ne contient pas au moins deux mots ou contient des caractères non alphabétiques.
    """

    new_line = line.split()
    if len(new_line) < 2:
        raise BadInputException("Ligne avec moins de deux mots.")

    for val in new_line:
        if not re.match(r'^[a-zA-Z]+$', val):
            raise BadInputException("Caractère non valide détecté.")

    try:
        result = sort_name(new_line)
        print(result)
    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":

    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                main(line.strip())
            except BadInputException:
                print("BAD INPUT")
sort_name("THIERRY GAILLARD")
