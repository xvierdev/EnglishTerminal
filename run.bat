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
    if exist "requirements.txt" (
        echo Installing dependencies from requirements.txt ...
        pip install -r requirements.txt
    ) else (
        echo Installing dependencies from pyproject.toml ...
        pip install keyboard
        pip freeze > requirements.txt
    )
    goto run
)

exit

:run
echo running program ...
python ./source/main.py    
