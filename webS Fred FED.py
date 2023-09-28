# WebS FED Fred

import requests
from bs4 import BeautifulSoup

# https://fred.stlouisfed.org/series/

print("\n                                                                                   UNRATE: unemployment rate                                                                \nDFF: Federal Funds Efectiveness Rate                                                                              \nMEDCPIM158SFRBCLE: Median Consumer Price Index                                             \nRRSF: Advance Real Retail and Food Services Sales                                                               \n                                                                                            \nPNRGINDEXM: Global price of Energy Index                                                            \nPNRGINDEXM: Global price of Energy Index                                                         \nPALLFNFINDEXM: Global Price Index of All Commodities                                                     \nPOILBREUSDM: Global price of Brent Crude                                                             \nIGREA: Index of Global Real Economic Activity                                                \nPFOODINDEXM: Global price of Food index\nQUSR628BIS: Real Residential Property Prices for United States                            \nWUIGLOBALSMPAVG: World Uncertainty Index: Global: Simple Average                                         \n                                                                           \nROWFDIQ027S: Rest of the World; Foreign Direct Investment in U.S.; Asset (Current Cost), Transactions                                                           \nA3274C0A144NBEA: Corporate profits after tax: Rest of the world                                               \n ")

caminho = str(input("Código FRED: "))

url_c = "https://fred.stlouisfed.org/series/" + caminho
page = requests.get(url_c)
soup_c = BeautifulSoup(page.content, 'html.parser')

valueB = cotac_m = float(soup_c.find(class_="series-meta-observation-value").get_text().replace(".","").replace(",","."))

print("\n",valueB)
print("\n", url_c)
