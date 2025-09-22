# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['classPrototype2.py'],
    pathex=[],
    binaries=[],
    datas=[('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\ImageHoverWidget2.py', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\resource_utils.py', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\altoclef.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\arrow.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\bassclef3.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\flat.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\natural.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\sharp.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\trebelclef.png', '.'), ('c:\\Users\\Jared Obid\\IBProjectMac\\jaredproj\\wholenote.png', '.')],
    hiddenimports=[],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MusicNotationApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
