import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Ruta de la imagen
img_path = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Paris.jpg'
output_folder = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Processed'

# Cargar la imagen a color
img = cv2.imread(img_path)

alpha = 1.5  # Factor de contraste
beta = 50  # Factor de brillo

new_image = np.clip(alpha * img + beta, 0, 255).astype('uint8')

filtered_image = cv2.medianBlur(new_image, 5)

gray_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Ruta completa del archivo de imagen de salida
output_path = os.path.join(output_folder, 'processed_image.jpg')

# Guardar la imagen procesada
cv2.imwrite(output_path, equalized_image)

# Mostrar las imágenes
plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(122)
plt.imshow(equalized_image, cmap='gray')
plt.title('Processed Image')

plt.show()
