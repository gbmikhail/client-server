"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

lines = [
    'сетевое программирование',
    'сокет',
    'декоратор'
]

with open('test_file.txt', 'w') as f:
    f.writelines('\n'.join(lines))

print(f.encoding)

file_coding = 'utf-8'
for _ in range(2):
    try:
        with open('test_file.txt', 'r', encoding=file_coding) as f:
            for i in f:
                print(i[:-1])
        break
    except UnicodeDecodeError as e:
        print(e)
    file_coding = locale.getpreferredencoding()
