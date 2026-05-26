import numpy as np
import imageio as iio

def color_to_grey(A) -> np.ndarray:
    """Charge une image depuis le chemin et la convertit en niveaux de gris.
    """
    im = iio.imread(A)
    if im.ndim == 2:
        return im
    return (im[:, :, :3] @ np.array([0.2989, 0.5870, 0.1140])).astype(np.uint8)


def gaussian_kernel(size: int = 5, sigma: float = 1.0) -> np.ndarray:
    """
    Génère un noyau gaussien 2D normalisé.
    """
    # Création d'un axe centré autour de 0
    ax = np.arange(-(size // 2), size // 2 + 1)

    # Création des coordonnées 2D
    xx, yy = np.meshgrid(ax, ax)

    # Formule de la gaussienne 2D
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))

    # Normalisation pour conserver les intensités
    kernel /= np.sum(kernel)

    return kernel


def convolution(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Applique une convolution entre une image
    et un noyau.
    """
    h, w = image.shape
    kh, kw = kernel.shape

    # Taille du padding
    pad_h = kh // 2
    pad_w = kw // 2

    # Ajout d'une bordure autour de l'image
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)),
                    mode='reflect')

    result = np.zeros_like(image, dtype=np.float32)

    # Inversion du noyau 
    kernel = np.flipud(np.fliplr(kernel))

    # Parcours des pixels
    for i in range(h):
        for j in range(w):

            # gestion voisinage
            region = padded[i:i + kh, j:j + kw]

            # Produit terme à terme + somme
            result[i, j] = np.sum(region * kernel)

    return result


def sobel_masks():
    """
    Retourne les masques de Sobel.
    """
    gx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    gy = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ], dtype=np.float32)

    return gx, gy


def prewitt_masks():
    """
    Retourne les masques de Prewitt.
    """
    gx = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)

    gy = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ], dtype=np.float32)

    return gx, gy