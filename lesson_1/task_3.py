"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

s1 = b'attribute'
s2 = b'класс'
s3 = b'функция'
s4 = b'type'

#     s2 = b'класс'
#         ^
# SyntaxError: bytes can only contain ASCII literal characters.

#     s3 = b'функция'
#         ^
# SyntaxError: bytes can only contain ASCII literal characters.
