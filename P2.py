import cv2
import os

# Ruta de la imagen
img_path = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Filtred\Gray Scale\processed_IMG_2313.jpeg'
output_folder = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Filtred\P2'

# Cargar la imagen en escala de grises
img = cv2.imread(img_path, 0)

# Verificar si la imagen se cargó correctamente
if img is not None:
    # Aplicar un filtro Gaussiano
    img_gauss = cv2.GaussianBlur(img, (5, 5), 0)

    # Aplicar un filtro de mediana
    img_median = cv2.medianBlur(img, 5)

    # Aplicar un filtro bilateral
    img_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    # Mostrar las imágenes
    cv2.imshow('Imagen Original', img)
    print('Mostrando -> Imagen Original')
    cv2.waitKey(0)
    cv2.imshow('Filtro Gaussiano', img_gauss)
    print('Mostrando -> Filtro Gaussiano')
    cv2.waitKey(0)
    cv2.imshow('Filtro de Mediana', img_median)
    print('Mostrando -> Filtro de Mediana')
    cv2.waitKey(0)
    cv2.imshow('Filtro Bilateral', img_bilateral)
    print('Mostrando -> Filtro Bilateral')
    cv2.waitKey(0)

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Guardar las imágenes procesadas
    cv2.imwrite(os.path.join(output_folder, 'gaussian.jpg'), img_gauss)
    cv2.imwrite(os.path.join(output_folder, 'median.jpg'), img_median)
    cv2.imwrite(os.path.join(output_folder, 'bilateral.jpg'), img_bilateral)

    # Esperar a que se presione una tecla y cerrar las ventanas
    print('Proceso terminado')
    cv2.destroyAllWindows()
else:
    print("No se pudo cargar la imagen:", img_path)

