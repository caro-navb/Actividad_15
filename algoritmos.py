import math

def distancia_euclidiana(x1, y1, x2, y2):
    distancia = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return distancia

