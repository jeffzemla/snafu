# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['interface.py'],
             pathex=['/Users/jcz/Dropbox/projects/semnet/snafu-gui/py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['IPython','matplotlib','mpl-data','notebook','pandas','libopenblasp-r0.3.7.dev','scipy','share','tornado'],
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
          name='interface',
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
               name='interface')
