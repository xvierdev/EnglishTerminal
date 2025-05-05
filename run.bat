@echo off

if exist "venv" (
    call venv/scripts/activate
    goto run
) else (
    echo Creating virtual environment ...
    python -m venv venv
    echo Activating virtual environment ...
    call venv/scripts/activate
    echo Upgrading pip ...
    python -m pip install --upgrade pip
    echo Updating dependencies
    pip install -r requirements.txt
    goto run
)

exit

:run
echo running program ...
python ./source/main.py    
