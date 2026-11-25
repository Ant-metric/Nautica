@echo off
REM Inicia o site local em http://127.0.0.1:8770 e abre o navegador.
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
    py _serve.py
) else (
    python _serve.py
)
pause
