SET mypath=%~dp0
REM INSTALA O PYTHON
%mypath%python\python373.exe /quiet InstallAllUsers=1 TargetDir=C:\Python\Python37 Include_pip=1 Include_test=0 PrependPath=1
REM PYTHON INSTALDO COM SUCESSO
REM ADICIONA AS BIBLIOTECAS UTILIZADAS
C:\Python\Python37\python.exe -m pip install beautifulsoup4
C:\Python\Python37\python.exe -m pip install requests
C:\Python\Python37\python.exe -m pip install pathlib
REM BIBLIOTECAS ADICIONADAS COM SUCESSO
setlocal
cd /d %~dp0
python web-scrapper.py