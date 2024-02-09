# Initialize venv
py -m venv .\venv

# Activate powershell script
.\.venv\Scripts\Activate.ps1

# Install Panda and Arrow
py -m pip install pandas 
py -m pip install numpy
py -m pip install seaborn
py -m pip install matplotlib 

# Execute freeze
py -m pip freeze > requirements.txt
