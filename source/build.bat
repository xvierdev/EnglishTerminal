@echo off
REM Script de Build para EnglishTerminal

echo Iniciando o build...

pyinstaller --name "EnglishTerminal" --onefile --add-data "modules;modules" --distpath="web-ui" main.py

if %errorlevel% equ 0 (
    echo Build concluído com sucesso!
) else (
    echo Erro durante o build. Verifique os logs do PyInstaller.
    pause
    exit /b %errorlevel%
)

echo Executável gerado em: web-ui\EnglishTerminal.exe
pause