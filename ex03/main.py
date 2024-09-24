#! /usr/bin/env python3
# coding: utf-8

from sys import argv
import math

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def compute_expression(a: float, b: float) -> float:
    """
    Calcule sqrt((sin(a)/a)*(sin(b)/b)) avec arrondi à 5 chiffres après la virgule.
    
        Parameters:
            a (float): Premier nombre flottant.
            b (float): Deuxième nombre flottant.
        
        Raises:
            ValueError: Si une erreur arithmétique se produit.
        
        Returns:
            float: La valeur arrondie à 5 chiffres après la virgule.
    """
    if a == 0 or b == 0:
        raise ValueError("ARITHMETIC ERROR")

    try:
        term_a = math.sin(a) / a
        term_b = math.sin(b) / b
        result = math.sqrt(term_a * term_b)
        return round(result, 5)
    except (ValueError, ZeroDivisionError, ArithmeticError):
        raise ValueError("ARITHMETIC ERROR")

def main(line: str):
    """
    Fonction principale qui traite une ligne d'entrée avec deux nombres flottants.
    
        Parameters:
            line (str): Une ligne contenant deux valeurs flottantes séparées par un espace.
    
        Returns:
            None: Affiche le résultat arrondi ou "ARITHMETIC ERROR" en cas d'erreur.
    """
    try:

        parts = line.strip().split()
        if len(parts) != 2:
            raise BadInputException("Input should contain exactly two float values.")
        

        a = float(parts[0])
        b = float(parts[1])
        

        result = compute_expression(a, b)
        print(result)
    except (ValueError, BadInputException):
        print("ARITHMETIC ERROR")
        exit(1)

if __name__ == "__main__":
    

    with open(argv[1]) as inputFile:
        for line in inputFile:
            main(line)
