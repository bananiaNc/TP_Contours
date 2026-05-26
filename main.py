import numpy as np
from PIL import Image
import fetch_image as fetchi
import sys

import filtre as fi

import gradient as grad

from hysteresis import hysteresis_threshold

from visualisation import (
    show_image,
    show_orientation,
    compare_filters
)



# Chargement de l'image
chemin = fetchi.fetch_image()
if chemin is None:
    print("Aucune image sélectionnée.")
    sys.exit()
    
image_grise = fi.color_to_grey(chemin)

# Lissage Gaussien
gaussian = fi.gaussian_kernel(size=5, sigma=1)

smoothed = fi.convolve2d(image_grise, gaussian)

# module de Sobel
sobel_x, sobel_y = fi.sobel_masks()

gx, gy, magnitude, orientation = grad.compute_gradient(
    smoothed,
    sobel_x,
    sobel_y
)

show_image(magnitude, "Module Sobel")

show_orientation(orientation)

nms = grad.non_maximum_suppression(magnitude, orientation)

show_image(nms, "Suppression des non-maxima")

edges_sobel = hysteresis_threshold(
    nms,
    low_threshold=20,
    high_threshold=40
)

show_image(edges_sobel, "Contours Sobel")

# Module de prewitt
prewitt_x, prewitt_y = fi.prewitt_masks()

_, _, magnitude_prewitt, orientation_prewitt = grad.compute_gradient(
    smoothed,
    prewitt_x,
    prewitt_y
)

nms_prewitt = grad.non_maximum_suppression(
    magnitude_prewitt,
    orientation_prewitt
)

edges_prewitt = hysteresis_threshold(
    nms_prewitt,
    low_threshold=20,
    high_threshold=40
)

# Comparaison Sobel / Prewitt
compare_filters(edges_sobel, edges_prewitt)