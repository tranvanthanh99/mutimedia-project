import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from convolution import convolution, convert_base64
from gaussian_smoothing import gaussian_blur


def sobel_edge_detection(image, filter, verbose=False):
    new_image_x = convolution(image, filter, verbose)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()

    new_image_y = convolution(image, np.flip(filter.T, axis=0), verbose)

    if verbose:
        plt.imshow(new_image_y, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()

    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    return gradient_magnitude


def run(filename):
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    image = cv2.imread(filename)
    image = gaussian_blur(image, 5, verbose=False)
    output_img = sobel_edge_detection(image, filter, verbose=False)

    return convert_base64(output_img, filename)

if __name__ == '__main__':
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    image = gaussian_blur(image, 5, verbose=True)
    output_img = sobel_edge_detection(image, filter, verbose=True)

    convert_base64(output_img, args["image"])