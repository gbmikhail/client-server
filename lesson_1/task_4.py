"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

lines = [
    'разработка',
    'администрирование',
    'protocol',
    'standard',
]

print('*' * 5, ' to bytes ', '*' * 5)
for idx, i in enumerate(lines):
    lines[idx] = i.encode('utf-8')
    print(lines[idx])

print('')
print('*' * 5, ' to str ', '*' * 5)
for idx, i in enumerate(lines):
    lines[idx] = i.decode('utf-8')
    print(lines[idx])
