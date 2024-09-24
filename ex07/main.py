#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def frequence_word(liste_mots) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            liste_mots : array
        
        Raises:
            
        
        Returns:
            result: str ; "mot1:frequence,mot2:frequence,mot_n:frequence"
            
    """

    result = ""

    frequence_mots = {}

    for mot in liste_mots:
        if mot in frequence_mots:
            frequence_mots[mot] += 1
        else:
            frequence_mots[mot] = 1
    
    result = ','.join([f"{mot}:{frequence}" for mot, frequence in frequence_mots.items()])

    return result

def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    
    ###
    new_line = line.lower()
    phrase = new_line.split(" ")
    for mots in phrase:
        if not re.match(r"^[a-zA-Z]+$", mots): raise BadInputException()
    phrase.sort()
    
    ### Frontal function call and exceptions management
    
    ###
    result = frequence_word(phrase)
    print(result)


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
