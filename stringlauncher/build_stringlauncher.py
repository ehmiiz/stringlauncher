import PyInstaller.__main__

PyInstaller.__main__.run([
    'stringlauncher.py',
    '--onefile',
    '--windowed',
    '--noconsole',
    '--icon=iconcolor.ico',
    '-n=StringLauncher'
])