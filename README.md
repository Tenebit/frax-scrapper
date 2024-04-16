Validador de derechos, ingresando a IPSA como un RPA

Primera vez, se debe crear el entorno. 

python3.11 -m venv env 

source env/bin/activate

pip install -r requirements.txt 
pip install "fastapi[all]"

uvicorn main:app --reload

http://127.0.0.1:8000/?tipo_documento=CC&numero_documento=71367081