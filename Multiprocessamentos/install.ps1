$Env:PYTHONPATH='' 
python -m venv venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip3 install poetry
poetry install
