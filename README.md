Validador de derechos, ingresando a IPSA como un RPA

Primera vez, se debe crear el entorno. 

python3.11 -m venv env 

source env/bin/activate

pip install -r requirements.txt 
pip install "fastapi[all]"

uvicorn main:app --reload

http://127.0.0.1:8000/?tipo_documento=CC&numero_documento=71367081

# Alternativa más fácil hacer request tipo POST, pero es posible que deje de funcionar bloqueando el dominio de tenebit, por eso mejor hicimos RPA
https://calculator.fraxplus.org/fraxScore

{
    "selectedLanguage": "",
    "selectedCountry": "28",
    "inputIdentificationText": "TEST",
    "inputAgeText": 70,
    "selectedSex": "M",
    "inputWeightText": "83",
    "inputHeightText": "181",
    "previousFracture": true,
    "parentFracturedHip": true,
    "currentlySmooking": true,
    "glucocorticoids": false,
    "rheumatoidArthritis": false,
    "secondaryOsteoporosis": false,
    "alcohol_3": false,
    "selectedFemoralNeckBMD": "",
    "inputFemoralNeckText": "",
    "inputFemoralNeckTextShow": "",
    "selectedUnit": "kg / cm",
    "selectedContinent": "3",
    "userId": 0
}