import cv2
import os

# Ruta de la imagen
img_path = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Filtred\Gray Scale\processed_IMG_2313.jpeg'
output_folder = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Filtred\P3'

# Cargar la imagen
img = cv2.imread(img_path)

# Verificar si la imagen se cargó correctamente
if img is not None:
    # Convertir la imagen a escala de grises
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ajustar el contraste y el brillo de la imagen
    img_contrast = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=50)

    # Mostrar las imágenes
    cv2.imshow('Imagen Original', img)
    print('Mostrando -> Imagen Original')
    cv2.waitKey(0)
    cv2.imshow('Imagen ajustada', img_contrast)
    print('Mostrando -> Imagen ajustada')
    cv2.waitKey(0)

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Guardar las imágenes procesadas
    cv2.imwrite(os.path.join(output_folder, 'original.jpg'), img)
    cv2.imwrite(os.path.join(output_folder, 'contrast.jpg'), img_contrast)

    # Esperar a que se presione una tecla y cerrar las ventanas
    print('Proceso terminado')
    cv2.destroyAllWindows()
else:
    print("No se pudo cargar la imagen:", img_path)
