#! /usr/bin/env python3
#coding : utf-8

from sys import argv
import re

class BadInputException(ValueError):
    """
    Raised when a given input does not fulfill the specification
    """
    pass

class TooLongException(ValueError):
    """
    Raised when a given input word is longer than 16 characters
    """
    pass

greetings = {"en":"Hello","fr":"Bonjour"}

def helloworld(lang: str, name: str) -> str:
    """
    Builds an internationalized greeting message as a string
    
        Parameters:
            lang (str): language code
            name (str): user name
        
        Raises:
            TooLongException: if name is longer than 16 characters
        
        Returns:
            (str): internationalized greeting message
    """

    if len(name)>16:
        raise TooLongException()
    
    return f'{greetings[lang]} {name}'.strip()

def main(line: str):
    
    ### Line parsing and BAD INPUT checking
    line_split = line.split(' ')
    if len(line_split) != 2 : raise BadInputException()
    lang, name = line_split
    if lang not in greetings: raise BadInputException()
    if not re.match(r"^[a-zA-Z]+$", name): raise BadInputException()
    ###
    
    
    ### Frontal function call and exceptions management
    try:
        print(helloworld(lang, name))
    except TooLongException:
        print("NAME TOO LONG")
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
