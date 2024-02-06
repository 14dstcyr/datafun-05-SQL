# dstcyr  datafun-05-SQL
# Initialize venv
py -m venv .venv

# Activate powershell script
.\.venv\Scripts\Activate.ps1

# Install Panda, numpy, seaborn
py -m pip install pandas 
py -m pip install numpy
py -m pip install seaborn
py -m pip install matplotlib

# Execute freeze dependencies
py -m pip freeze > requirements.txt

