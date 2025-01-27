from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageFilter

def process_image():
    # Открываем файл через диалоговое окно
    file_path = askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All files", "*.*")])
    if not file_path:
        print("Файл не выбран")
        return

    try:
        # Открытие изображения
        img = Image.open(file_path).convert("RGBA")  # Режим 32 бита с альфа-каналом
        print(f"Размер: {img.size}, Формат: {img.format}")

        # Поворот изображения на произвольный угол
        angle = float(input("Введите угол поворота: "))
        img_rotated = img.rotate(angle, expand=True)

        # Применение фильтра EMBOSS
        img_filtered = img_rotated.filter(ImageFilter.EMBOSS)

        # Создание миниатюры
        thumbnail_size = (100, 100)
        thumbnail = img_filtered.copy()
        thumbnail.thumbnail(thumbnail_size)

        # Вставка миниатюры в правый нижний угол
        img_filtered.paste(thumbnail, (img_filtered.width - thumbnail.width, img_filtered.height - thumbnail.height), thumbnail)

        # Сохранение результата
        save_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            img_filtered.save(save_path)
            print(f"Изображение сохранено по пути: {save_path}")
        else:
            print("Сохранение отменено")

    except Exception as e:
        print(f"Ошибка обработки изображения: {e}")

if __name__ == "__main__":
    process_image()
