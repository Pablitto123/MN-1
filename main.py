import math
import numpy as nu
import numpy.linalg
import scipy

def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r >= 0 and h >= 0:
        return 2 * math.pi * r * (r + h)
    else:
        return float('nan')


def fib(n: int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if type(n) == int and n > 0:
        arr = nu.empty(n)
        arr[0] = 1
        if n > 1:
            arr[1] = 1
        if n > 2:
            for i in range(n - 2):
                arr[i + 2] = arr[i + 1] + arr[i]
        return arr #w teście dla 15 wektor jest zapakowany w inny wektor, a dla 1 nie. Dlatego test dla 15 nie przechodzi, ponadto ciąg fibonaciego zaczyna się od 0 a nie od 1. :)
    return None


def matrix_calculations(a: float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    if not isinstance(a, (int, float)):
        return None

    matrix = nu.array([[a, 1, -a], [0, 1, 1],  [-a, a, 1]])
    Mdet = nu.linalg.det(matrix)
    if Mdet != 0:
        Minv = nu.linalg.inv(matrix)
    else:
        Minv = nu.array('NaN')
    Mt = nu.transpose(matrix)
    return tuple([Minv, Mt, Mdet])




def custom_matrix(m: int, n: int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    return None
