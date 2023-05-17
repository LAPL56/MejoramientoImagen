import cv2
import os

img_path = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\IMG_2313.jpeg'
output_folder = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Filtred\P1'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(img, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
opened = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)

scale_percent = 25
width = int(opened.shape[1] * scale_percent / 100)
height = int(opened.shape[0] * scale_percent / 100)
dim = (width, height)

dst = cv2.resize(opened, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Imagen mejorada', dst)
cv2.imwrite('nombre_imagen_mejorada.jpg', dst)

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Ruta completa del archivo de imagen de salida
output_path = os.path.join(output_folder, 'processed_kernel.png')

# Guardar la imagen procesada
cv2.imwrite(output_path, dst)

# Guardar la imagen procesada
cv2.imwrite(output_path, dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
