# -*- mode: python -*-

block_cipher = None


a = Analysis(['PirateScope'],
             pathex=['C:\\Users\\tomek001\\workspacePython27\\PirateScope'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PirateScope',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='data-wave.ico')
