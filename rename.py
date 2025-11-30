import os

for filename in os.listdir('.'):
    if filename.endswith('.jpg') and 'page-' in filename:
        # извлекаем исходный номер
        old_num = int(filename.split('page-')[1].split('.jpg')[0])
        
        # корректируем: страница = файл - 1
        new_num = old_num - 1
        
        # форматируем в 4 цифры
        new_name = f"page-{new_num:04}.jpg"
        
        print(f"{filename} → {new_name}")
        os.rename(filename, new_name)
