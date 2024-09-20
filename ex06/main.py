#!/usr/bin/env python3
# coding: utf-8

import csv
import os
from sys import argv

class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def read_csv_file(file_path: str) -> list:
    """
    Lit un fichier CSV et retourne son contenu sous forme de liste de listes.
    
        Parameters:
            file_path (str): Le chemin du fichier CSV.
        
        Returns:
            list: Une liste de listes contenant les valeurs du fichier CSV.
        
        Raises:
            BadInputException: Si le fichier CSV est mal formé ou contient des erreurs.
    """
    if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
        raise BadInputException("BAD INPUT")
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
    
    print("CSV Data:", data)  # Debug: Afficher le contenu du CSV
    
    # Check if the CSV is properly formatted with only numeric values
    try:
        for row in data[1:]:  # Skip the header row
            for cell in row:
                try:
                    float(cell)  # Try to convert each cell to float
                except ValueError:
                    raise BadInputException("BAD INPUT")
    except Exception as e:
        raise BadInputException(f"CSV Format Error: {e}")
    
    return data

def get_column_indices(headers: list, column_names: list) -> list:
    """
    Obtient les indices des colonnes correspondant aux noms donnés.
    
        Parameters:
            headers (list): La liste des en-têtes de colonnes.
            column_names (list): La liste des noms de colonnes à rechercher.
        
        Returns:
            list: Les indices des colonnes correspondantes.
        
        Raises:
            BadInputException: Si un des noms de colonnes n'est pas trouvé dans les en-têtes.
    """
    indices = []
    for name in column_names:
        if name not in headers:
            raise BadInputException(f"Column {name} not found in headers")
        indices.append(headers.index(name))
    return indices

def compute_sum_of_products(data: list, start_row: int, end_row: int, column_indices: list) -> float:
    """
    Calcule la somme des produits des valeurs dans les lignes spécifiées.
    
        Parameters:
            data (list): Les données du fichier CSV.
            start_row (int): La ligne de début (incluse).
            end_row (int): La ligne de fin (incluse).
            column_indices (list): Les indices des colonnes à multiplier.
        
        Returns:
            float: La somme des produits des valeurs.
    """
    total_sum = 0.0
    for row in data[start_row:end_row + 1]:
        product = 1.0
        for idx in column_indices:
            try:
                product *= float(row[idx])
            except IndexError:
                raise BadInputException(f"Index {idx} out of range in row")
            except ValueError:
                raise BadInputException(f"Non-numeric value encountered in row")
        total_sum += product
    return total_sum

def frontal_function(line: str) -> float:
    """
    Fonction principale pour traiter la ligne d'entrée.
    
        Parameters:
            line (str): Une ligne contenant M, N, une liste de mots, et un chemin de fichier.
        
        Returns:
            float: La somme des produits des valeurs ou "BAD INPUT" en cas d'erreur.
    """
    parts = line.strip().split()
    if len(parts) < 4:
        raise BadInputException("Insufficient input parts")
    
    try:
        M = int(parts[0])
        N = int(parts[1])
        if M > N:
            raise BadInputException("M is greater than N")
        column_names = parts[2:-1]
        file_path = parts[-1]
        
        data = read_csv_file(file_path)
        
        if len(data) <= N:
            raise BadInputException("N exceeds number of data rows")
        
        headers = data[0]
        rows = data[1:]
        
        column_indices = get_column_indices(headers, column_names)
        
        total_sum = compute_sum_of_products(rows, M, N, column_indices)
        
        return round(total_sum, 2)
    
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
    try:
        result = frontal_function(line)
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
