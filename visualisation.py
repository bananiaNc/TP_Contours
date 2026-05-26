"""
visualization.py
----------------

Fonctions d'affichage et de visualisation.
"""

import matplotlib.pyplot as plt
import numpy as np


def show_image(image, title="Image", cmap="gray"):
    """
    Affiche une image.
    """

    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()


def show_orientation(orientation):
    """
    Affiche la carte des orientations.
    """

    plt.figure(figsize=(6, 6))
    plt.imshow(orientation, cmap='hsv')
    plt.colorbar(label='Orientation (degrés)')
    plt.title("Orientation du gradient")
    plt.axis("off")
    plt.show()


def compare_filters(sobel, prewitt):
    """
    Compare les résultats Sobel et Prewitt.
    """

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].imshow(sobel, cmap='gray')
    ax[0].set_title("Sobel")
    ax[0].axis("off")

    ax[1].imshow(prewitt, cmap='gray')
    ax[1].set_title("Prewitt")
    ax[1].axis("off")

    plt.show()