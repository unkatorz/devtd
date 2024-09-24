#! /usr/bin/env python3
# coding: utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def convert_to_compact_notation(value: str):
    """
    Convertit une valeur de type Integer ou Float vers sa représentation la plus compacte.
    
        Parameters:
            value (str): La chaîne de caractères représentant un nombre.
        
        Raises:
            BadInputException: Si l'entrée n'est pas un nombre valide.
        
        Returns:
            str: La représentation compacte du nombre en notation classique ou scientifique.
    """
    value = value.strip()


    if re.match(r'^-?\d+(\.\d+)?$', value):
        try:

            if '.' in value:
                number = float(value)

                sci_notation = "{:e}".format(number)
                if len(sci_notation) < len(value):
                    return sci_notation
                else:
                    return str(number)
            else:
                number = int(value)
                return str(number)
        except ValueError:
            raise BadInputException("Input is not a valid number.")
    else:
        raise BadInputException("Input is not a valid number format.")

def main(line: str):
    """
    Fonction principale qui vérifie la ligne et convertit le nombre vers sa représentation compacte.
    
        Parameters:
            line (str): Une ligne de l'entrée.
    
        Returns:
            None: Affiche le résultat ou "BAD INPUT" en cas d'erreur.
    """
    try:
        result = convert_to_compact_notation(line)
        print(result)
    except BadInputException:
        print("BAD INPUT")

if __name__ == "__main__":
    

    with open(argv[1]) as inputFile:
        for line in inputFile:
            main(line)
