import requests 
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# Åpen API funnet på https://exchangeratesapi.io/, flere API-er kan finnes her: https://github.com/public-apis/public-apis#calendar
# Status på API-en kan sjekkes her: https://stats.uptimerobot.com/Q6z9gTYrY
# Dette er et eksempel på hvordan man kan bruke en GET request for å motta data fra en API

valuta = "NOK"
res_nok = requests.get('https://api.exchangeratesapi.io/latest', params={"base": valuta}) # Valutapriser relativt til den norske kronen, API-en forventer et parameter som heter base der vi spesifiserer hvilken grunnvaluta vi skal bruke
print(res_nok.status_code) # Forhåpentligvis 200. 200 betyr OK

res_nok_dict = res_nok.json() # Dataen kommer tilbake i json-format. Bruk .json() på responsen for å konvertere til et python-dictionary

print(f'1 NOK = {res_nok_dict["rates"]["USD"]:.2f} USD') # Antall USD man får for én norsk krone, prøv også GBP, DKK osv..

# ---------------------------------------------------------

start_at = "2019-01-01"
end_at = "2019-11-13"
base="NOK"

res_nok_hist = requests.get("https://api.exchangeratesapi.io/history", params={"start_at": start_at, "end_at": end_at, "base": base})

print(res_nok_hist.status_code) # Forhåpentligvis 200. 200 betyr OK
print(res_nok_hist.json()["rates"])


usd_values = []
for key, val in res_nok_hist.json()["rates"].items():
    usd_values.append(val["USD"])

print(usd_values)

usd_values_smoothed = savgol_filter(usd_values, 41, 2) # Vindu på 41 dager, polynom av 2. orden

axes = plt.axes()
plt.plot(usd_values)
plt.plot(usd_values_smoothed)
plt.title("1 NOK to USD")
plt.xlabel("Day")
plt.ylabel("USD")
axes.set_ylim([0.1, 0.13])
plt.show()