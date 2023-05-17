import cv2
import os

folder_path = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted'
output_folder = r'C:\Users\LAPL\OneDrive\Documentos\ARTEK\Cuarto Trimestre\PDI\Converted\Filtred\Gray Scale'

# Obtener la lista de archivos en la carpeta
file_list = os.listdir(folder_path)

# Iterar sobre cada archivo
for filename in file_list:
    if filename.endswith('.jpeg'):  # Asegurarse de procesar solo archivos JPEG (puedes ajustar la extensión según tus necesidades)
        # Ruta completa del archivo de imagen de entrada
        input_path = os.path.join(folder_path, filename)

        # Leer la imagen en escala de grises
        img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

        # Aplicar los filtros
        # Aplicar filtro de suavizado
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        # Aplicar umbral adaptativo
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        # Aplicar transformación morfológica
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        # Aplicar transformación de apertura
        opened = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)

        # Redimensionar la imagen
        scale_percent = 25
        width = int(opened.shape[1] * scale_percent / 100)
        height = int(opened.shape[0] * scale_percent / 100)
        dim = (width, height)
        dst = cv2.resize(opened, dim, interpolation=cv2.INTER_AREA)

        # Ruta completa del archivo de imagen de salida
        output_path = os.path.join(output_folder, 'processed_' + filename)

        # Guardar la imagen procesada
        cv2.imwrite(output_path, dst)

        # Mostrar imagen mejorada y guardarla
        cv2.imshow('Imagen procesada', dst)
        cv2.waitKey(0)

print("Proceso completado")
cv2.destroyAllWindows()