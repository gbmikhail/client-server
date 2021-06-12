"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""
import subprocess

ping_resources = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']
]

for ping_now in ping_resources:
    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    for line in ping_process.stdout:
        line = line.decode('cp866').encode('utf-8')
        # Обрезаем \r\n
        line = line.decode('utf-8')[:-2]
        print(line)
