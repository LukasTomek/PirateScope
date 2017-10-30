set ZIP="C:\Program Files\7-Zip\7z.exe"

pyinstaller release-onefile.spec --upx-dir C:\Tools\upx393w

rem pyinstaller test.spec --upx-dir C:\Tools\upx393w

rem pyinstaller CodeTranslator.py --nowindowed --icon=translate_icon_crop_resize.ico --onefile
pause