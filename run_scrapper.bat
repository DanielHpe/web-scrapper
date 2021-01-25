SET mypath=%~dp0
REM ADICIONA AS BIBLIOTECAS UTILIZADAS
C:\Python\Python37\python.exe -m pip install beautifulsoup4
C:\Python\Python37\python.exe -m pip install requests
C:\Python\Python37\python.exe -m pip install pathlib
REM BIBLIOTECAS ADICIONADAS COM SUCESSO
setlocal
cd /d %~dp0
python web-scrapper.py