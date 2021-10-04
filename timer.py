#pip install playsound
import time
from playsound import playsound


def count(num):
    while num:
        minuts, sec = divmod(num, 60)#подсмотрел divmod
        timer = f'{minuts}:{sec}'
        print(timer)
        time.sleep(1)
        num -= 1
    playsound('sound.mp3')
    '''после озвучки поялвяется ошибка Error 263 for command:
        close sound.mp3
    Указанное устройство не открыто или не опознается интерфейсом MCI.
    Failed to close the file: sound.mp3'''


def countdown(mins, seconds):
    if mins == 0:
        count(seconds)

    else:
        count(mins * 60 + seconds)


countdown(int(input('Enter the minuts')), int(input('Enter the seconds')))
