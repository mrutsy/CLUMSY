:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
:: Execute stuff...

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python not installed

:: powershell.exe -Command (new-object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe','python.exe')
python modules/server.py $@
pause