# Chinese Virus 🚩

Make a new .exe file in `Chinese_Virus/dist` directory from `Chinese_Virus` directory (requires **PyInstaller**):<br/>

`pyinstaller --onefile --noconsole --add-data="data;data" --icon=China.ico --name=Chinese_Virus Chinese_Virus_Core/__main__.py`

Program saves your desktop files to `C:\Users\YOURNAME\CCP_desktop_files.zip`