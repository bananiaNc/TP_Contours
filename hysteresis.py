"""
hysteresis.py
-------------

Implémentation du seuillage par hystérésis.
"""

import numpy as np


def hysteresis_threshold(image, low_threshold, high_threshold):
    """
    Applique un seuillage par hystérésis.
    """

    h, w = image.shape

    result = np.zeros((h, w), dtype=np.uint8)

    # Pixels forts
    strong = 255

    # Pixels faibles
    weak = 50

    # Détection des pixels forts/faibles
    strong_i, strong_j = np.where(image >= high_threshold)
    weak_i, weak_j = np.where(
        (image >= low_threshold) &
        (image < high_threshold)
    )
    result[strong_i, strong_j] = strong
    result[weak_i, weak_j] = weak
    
    # Connexité 8-voisins
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if result[i, j] == weak:
                # Si un voisin est fort, le pixel devient contour
                if np.any(result[i - 1:i + 2, j - 1:j + 2] == strong):
                    result[i, j] = strong
                else:
                    result[i, j] = 0

    return result