# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['classPrototype2.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/jared/Music-Note-Transposer/ImageHoverWidget2.py', '.'), ('/Users/jared/Music-Note-Transposer/resource_utils.py', '.'), ('/Users/jared/Music-Note-Transposer/altoclef.png', '.'), ('/Users/jared/Music-Note-Transposer/arrow.png', '.'), ('/Users/jared/Music-Note-Transposer/bassclef3.png', '.'), ('/Users/jared/Music-Note-Transposer/flat.png', '.'), ('/Users/jared/Music-Note-Transposer/natural.png', '.'), ('/Users/jared/Music-Note-Transposer/sharp.png', '.'), ('/Users/jared/Music-Note-Transposer/trebelclef.png', '.'), ('/Users/jared/Music-Note-Transposer/wholenote.png', '.')],
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
    name='NoteTranspositionProgram',
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
app = BUNDLE(
    exe,
    name='NoteTranspositionProgram.app',
    icon=None,
    bundle_identifier=None,
)
