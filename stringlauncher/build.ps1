if (Get-Command pyinstaller*) {
    $Command = 'pyinstaller --onefile --noconsole main.py --icon=iconcolor.ico -n StringLauncher'
    Invoke-Command -Command $Command
}
else {
    Write-Error "pyinstaller is not present in PATH." -ErrorAction Stop
}