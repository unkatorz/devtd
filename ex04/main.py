#! /usr/bin/env python3
# coding: utf-8

from sys import argv

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def frontal_function(dna_sequence: str) -> str:
    """
    Convertit une séquence ADN en ARN.
    
        Parameters:
            dna_sequence (str): Une séquence ADN.
        
        Raises:
            BadInputException: Si la séquence contient des caractères non valides.
        
        Returns:
            str: La séquence ARN en majuscules ou "NOT A DNA SEQUENCE" si la séquence n'est pas valide.
    """
    valid_chars = set("ACGTacgt")
    
    if all(char in valid_chars for char in dna_sequence):
        rna_sequence = dna_sequence.upper().replace('T', 'U')
        return rna_sequence
    else:
        raise BadInputException("NOT A DNA SEQUENCE")

def main(line: str):
    """
    Traite une ligne d'entrée et convertit une séquence ADN en ARN.
    
        Parameters:
            line (str): Une ligne contenant une séquence ADN.
    
        Returns:
            None: Affiche la séquence ARN ou "NOT A DNA SEQUENCE" en cas d'erreur.
    """
    # Nettoyer la ligne d'entrée
    dna_sequence = line.strip()
    
    try:
        # Appeler la fonction principale pour la conversion
        result = frontal_function(dna_sequence)
        print(result)
    except BadInputException as e:
        print(e)


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
