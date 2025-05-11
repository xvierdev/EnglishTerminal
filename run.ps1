# Define the virtual environment name
$VenvName = "venv"

# Define the requirements file name
$RequirementsFile = "requirements.txt"

# Define the path to the activate script
$ActivateScript = "$VenvName/Scripts/activate"

# Check if the virtual environment directory exists
if (Test-Path -Path $VenvName -PathType Container) {
    # Activate the virtual environment
    Write-Host "Activating virtual environment '$VenvName'..."
    .$ActivateScript
}
else {
    # Create the virtual environment
    Write-Host "Creating virtual environment '$VenvName'..."
    python -m venv $VenvName

    # Activate the virtual environment
    Write-Host "Activating virtual environment '$VenvName'..."
    .$ActivateScript

    # Upgrade pip
    Write-Host "Upgrading pip..."
    python -m pip install --upgrade pip

    # Install dependencies from requirements.txt
    Write-Host "Updating dependencies..."
    if (Test-Path -Path $RequirementsFile -PathType Leaf) {
        pip install -r $RequirementsFile
    }
    else {
        Write-Host "Warning: '$RequirementsFile' not found. Install default dependencies..."
        pip install keyboard
        pip freeze > $RequirementsFile
        Write-Host "Dependencies installed and saved to '$RequirementsFile'."
    }
}

# Run the program
Write-Host "Running program..."
python ./source/main.py
deactivate