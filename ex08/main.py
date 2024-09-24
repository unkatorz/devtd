#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def concaten(liste, k: int) :
    """
    Rename and document this function accordingly.
    
        Parameters:
            liste : array ; 

            k : int
        
        Raises:
            
        
        Returns:
            
    """
    resultat = ""
    for i in range(1, k + 1):
        mots = []

        # Parcourir les diviseurs et leurs mots associés
        for diviseur, mot in liste.items():
            if i % int(diviseur) == 0:
                mots.append(mot)

        # Affiche l'entier ou la concaténation des mots associés
        if mots:
            resultat += "".join(mots)+"\n"
        else:
            resultat += str(i)+"\n"

    return resultat

def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    
    ###
    couple = {}
    liste_couple = []
    tableau = line.split(" ")
    k = int(tableau[-1])
    if k < 0: raise BadInputException() 
    #print(len(tableau))
    for i in range(0,len(tableau)-1,2):
        #print(tableau[i], tableau[i+1])
        if int(tableau[i]) in tableau: raise BadInputException()

        if not int(tableau[i]) > 0: raise BadInputException()
        
        if not re.match(r"^[a-zA-Z]+$", tableau[i+1]): raise BadInputException()
        
        couple[tableau[i]] = tableau[i+1]

    #print(liste_couple)
    ### Frontal function call and exceptions management
    result = concaten(couple,k)
    print(result)
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
