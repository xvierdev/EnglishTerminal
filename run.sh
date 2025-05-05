#!/bin/bash

set +x 

run_application(){
    echo "running program ..."
    python ./source/main.py
    deactivate
}

activate_venv(){
    if [ -d "bin" ]; then
        source venv/bin/activate
    else
        source venv/Scripts/activate
    fi
}

if [ -d "venv" ]; then
    activate_venv
else
    echo "Creating virtual environment ..."
    python -m venv venv
    echo "Activating virtual environment ..."
    activate_venv
    echo "Upgrading pip ..."
    python -m pip install --upgrade pip
    echo "Updating dependencies"
    pip install -r requirements.txt
    run_application
fi