from PIL import Image, ImageFilter
import cv2
import numpy as np

def apply_transformations(input_image_path, output_image_path):
    # Открываем изображение
    img = Image.open(input_image_path)

    # Перенос изображения
    numpy_image = np.array(img)
    rows, cols, _ = numpy_image.shape
    M_translation = np.float32([[1, 0, 50], [0, 1, 50]])  # Перенос на 50 пикселей вправо и вниз
    translated_image = cv2.warpAffine(numpy_image, M_translation, (cols, rows))

    # Преобразование в LAB
    lab_image = cv2.cvtColor(translated_image, cv2.COLOR_RGB2LAB)

    # Применение фильтра с маской 5x5 (Prewitt)
    kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    prewitt_x = cv2.filter2D(lab_image, -1, kernel_x)
    prewitt_y = cv2.filter2D(lab_image, -1, kernel_y)
    prewitt_combined = cv2.add(prewitt_x, prewitt_y)

    # Конвертируем обратно для сохранения
    final_image = Image.fromarray(cv2.cvtColor(prewitt_combined, cv2.COLOR_LAB2RGB))

    # Сохраняем результат
    final_image.save(output_image_path)

# Путь к входному и выходному изображениям
input_image = "input_image.jpg"  # Замените на имя вашего файла
output_image = "output_image.jpg"

# Выполняем обработку
apply_transformations(input_image, output_image)

print("Изображение обработано и сохранено как", output_image)
