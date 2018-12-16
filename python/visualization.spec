# -*- mode: python -*-

block_cipher = None


a = Analysis(['visualization.py'],
             pathex=['C:\\Program Files\\Python36', 'config.py', 'dsp.py', 'gui.py', 'led.py', 'melbank.py', 'melbank.py', 'microphone.py', 'F:\\python\\audio-reactive-led\\python'],
             binaries=[],
             datas=[],
             hiddenimports=['numpy','config','melbank','pyqtgraph'],
             hookspath=[],
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
          name='visualization',
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
               name='visualization')
