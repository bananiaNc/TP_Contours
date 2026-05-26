import numpy as np
from filtre import convolve2d

def compute_gradient(image, mask_x, mask_y):
    """
    Calcule le gradient d'une image.
    """

    # Calcul des dérivées
    gx = convolve2d(image, mask_x)
    gy = convolve2d(image, mask_y)

    # Module du gradient
    magnitude = np.sqrt(gx**2 + gy**2)

    # Orientation du gradient en degrés
    orientation = np.rad2deg(np.arctan2(gy, gx))

    return gx, gy, magnitude, orientation

def non_maximum_suppression(magnitude, orientation):
    """
    Supprime les pixels qui ne sont pas des maxima locaux.
    """

    h, w = magnitude.shape

    result = np.zeros((h, w), dtype=np.float32)

    # Parcours de l'image (sans les bords)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            angle = orientation[i, j]
            current = magnitude[i, j]
            if (-22.5 <= angle < 22.5) or (157.5 <= angle <= 180) or (-180 <= angle < -157.5):
                q = magnitude[i, j + 1]
                r = magnitude[i, j - 1]
            elif (22.5 <= angle < 67.5) or (-157.5 <= angle < -112.5):
                q = magnitude[i + 1, j - 1]
                r = magnitude[i - 1, j + 1]
            elif (67.5 <= angle < 112.5) or (-112.5 <= angle < -67.5):
                q = magnitude[i + 1, j]
                r = magnitude[i - 1, j]
            else:
                q = magnitude[i - 1, j - 1]
                r = magnitude[i + 1, j + 1]

            # Conservation uniquement des maxima locaux
            if current >= q and current >= r:
                result[i, j] = current

    return result