import cv2
import numpy as np
from scipy import ndimage

# Bildpfad vom Benutzer eingeben
file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

# Bild in Graustufen lesen
input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Gradient Operator
grad_x = cv2.Sobel(input_image, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(input_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_operator = cv2.magnitude(grad_x, grad_y)
cv2.imwrite("gradient-operator.jpg", gradient_operator)

# Sobel Operator
sobel_x = cv2.Sobel(input_image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(input_image, cv2.CV_64F, 0, 1, ksize=5)
sobel_operator = cv2.magnitude(sobel_x, sobel_y)
cv2.imwrite("sobel-operator.jpg", sobel_operator)

# Canny Operator
canny_operator = cv2.Canny(input_image, 100, 200)
cv2.imwrite("canny-operator.jpg", canny_operator)

# Laplace Operator
laplacian_operator = cv2.Laplacian(input_image, cv2.CV_64F)
cv2.imwrite("laplace-operator.jpg", laplacian_operator)
