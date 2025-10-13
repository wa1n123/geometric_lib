import math


def area(r):
    """
    Вычисляет площадь круга.
    
    Parameters:
        r (float): Радиус круга
        
    Returns:
        float: Площадь круга по формуле π * r^2
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности (периметр круга).
    
    Parameters:
        r (float): Радиус круга
        
    Returns:
        float: Длина окружности по формуле 2 * π * r
    """
    return 2 * math.pi * r