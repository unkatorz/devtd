#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def search_word(chaine:str, chemin:str) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            chaine : string ; La chaîne recherché
            
            chemin : string ; Le chemin du fichier voulu
        
        Raises:
            
        
        Returns:

            resultats : string ; Tous les mots correspondants à la chaine recherché.
            
    """
    
    with open(chemin, 'r') as file:
        content = file.read()

    motif = chaine.replace('*','.*')

    regex = re.compile(motif)

    liste_chaine = content.split()

    resultats = [mot for mot in liste_chaine if regex.search(mot)]

    return " ".join(resultats)


def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    
    ###
    
    parameter = line.split(" ")

    chaine = parameter[0]
    chemin = parameter[1]

    if not re.match(r"[a-zA-Z\*]+", chaine): raise BadInputException
    with open(chemin, 'r') as file:
        content = file.read()
        if not re.match(r"[a-zA-Z]*", content): raise BadInputException



    ### Frontal function call and exceptions management
    try:

        result = search_word(chaine, chemin)
        print(result)
    except:
        print("NOK")
    ###


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
