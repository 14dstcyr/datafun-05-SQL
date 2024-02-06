# Initialize venv
py -m venv .venv

# Activate powershell script
.\.venv\Scripts\Activate.ps1

# Install Panda and Arrow
py -m pip install pandas pyarrow

# Execute freeze
py -m pip freeze > requirements.txt
