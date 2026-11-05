@echo off
setlocal
cd /d "%~dp0"

set "PYTHON=python"
if exist ".venv\Scripts\python.exe" set "PYTHON=.venv\Scripts\python.exe"

%PYTHON% -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Streamlit is not installed in the selected Python environment.
    echo Install project dependencies with:
    echo %PYTHON% -m pip install -r requirements.txt
    pause
    exit /b 1
)

%PYTHON% -m streamlit run app.py
if errorlevel 1 pause