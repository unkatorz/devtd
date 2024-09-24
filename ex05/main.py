#!/usr/bin/env python3
# coding: utf-8

from sys import argv

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def is_valid_dna_sequence(sequence: str) -> bool:
    """
    Vérifie si une séquence ADN est valide.
    
        Parameters:
            sequence (str): La séquence ADN.
        
        Returns:
            bool: True si la séquence est valide, False sinon.
    """
    valid_chars = set("ACGTacgt")
    return all(char in valid_chars for char in sequence)

def find_occurrences(a: str, b: str):
    """
    Trouve les occurrences de la séquence ADN A dans la séquence ADN B.
    
        Parameters:
            a (str): La séquence ADN à rechercher.
            b (str): La séquence ADN dans laquelle rechercher.
        
        Returns:
            list or bool: Une liste d'entiers avec le nombre d'occurrences et les positions ou False si A n'existe pas dans B.
    """
    if not (is_valid_dna_sequence(a) and is_valid_dna_sequence(b)):
        raise BadInputException("BAD INPUT")
    

    a = a.upper()
    b = b.upper()
    

    positions = []
    start = 0
    while True:
        start = b.find(a, start)
        if start == -1:
            break
        positions.append(start)
        start += len(a)
    
    if positions:
        return [len(positions)] + positions
    else:
        return False

def frontal_function(line: str):
    """
    Fonction principale pour traiter la ligne d'entrée.
    
        Parameters:
            line (str): Une ligne contenant deux séquences ADN séparées par un espace.
        
        Returns:
            str or list or bool: La liste des occurrences ou False ou "BAD INPUT" en cas d'erreur.
    """
    parts = line.strip().split()
    if len(parts) != 2:
        raise BadInputException("BAD INPUT")
    
    a, b = parts
    try:
        result = find_occurrences(a, b)
        if result is False:
            return False
        else:
            return ','.join(map(str, result))
    except BadInputException as e:
        return str(e)

def main(line: str):
    """
    Traite une ligne d'entrée et appelle frontal_function.
    
        Parameters:
            line (str): Une ligne d'entrée.
    
        Returns:
            None: Affiche le résultat ou l'erreur.
    """
    result = frontal_function(line)
    if result:
        print(result)
    else:
        print("False")


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
