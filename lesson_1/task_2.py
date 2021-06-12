"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

lines = (
    b'class',
    b'function',
    b'method',
)

for i in lines:
    print(type(i), f'len = {len(i)}', i)
