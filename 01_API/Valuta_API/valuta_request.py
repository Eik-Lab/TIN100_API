import requests 

# Åpen API funnet på https://exchangeratesapi.io/
# Status på API-en kan sjekkes her: https://stats.uptimerobot.com/Q6z9gTYrY
# Dette er et eksempel på hvordan man kan bruke en GET request for å motta data fra en API

valuta = "NOK"
res = requests.get(f'https://api.exchangeratesapi.io/latest', params={"base": valuta}) # Valutapriser relativt til den norske kronen, API-en forventer et parameter som heter base der vi spesifiserer hvilken grunnvaluta vi skal bruke
print(res.status_code) # Forhåpentligvis 200. 200 betyr OK

res_dict = res.json() # Dataen kommer tilbake i json-format. Bruk .json() på responsen for å konvertere til et python-dictionary

print(f'1 NOK = {res_dict["rates"]["USD"]:.2f} USD') # Antall USD man får for én norsk krone, prøv også GBP, DKK osv..