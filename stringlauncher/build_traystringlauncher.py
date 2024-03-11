import PyInstaller.__main__

PyInstaller.__main__.run([
    'stringlauncher.py',
    '--onefile',
    '--noconsole',
    '--icon=favicon.ico',
    '--add-data="favicon.ico;."',
    '--name=TrayStringLauncher'
])