# config.py

import os
from pathlib import Path

possible_desktop_paths = [Path(os.environ['USERPROFILE']) / 'Desktop', Path(os.environ['USERPROFILE']) / 'Рабочий стол', Path(os.environ['USERPROFILE']) / 'OneDrive' / 'Desktop', Path(os.environ['USERPROFILE']) / 'OneDrive' / 'Рабочий стол']
for desktop_path in possible_desktop_paths:
    if Path.exists(desktop_path):
        PATH_TO_DESKTOP = desktop_path
        break

PATH_TO_DATA = Path('/'.join(__file__.replace('\\', '/').split('/') [:-2])) / 'data'
PATH_TO_MAIN = PATH_TO_DATA / 'main'
PATH_TO_IMAGES = PATH_TO_DATA / 'images'
PATH_TO_TEXT = PATH_TO_DATA / 'text'


__all__ = ['PATH_TO_DATA', 'PATH_TO_MAIN', 'PATH_TO_IMAGES', 'PATH_TO_TEXT', 'PATH_TO_DESKTOP']