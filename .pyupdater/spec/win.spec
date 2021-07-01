# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\Pyuptests\\Interface.py'],
             pathex=['E:\\Pyuptests', 'E:\\Pyuptests\\.pyupdater\\spec'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['e:\\software\\archivos de programas e\\anaconda\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='win')
