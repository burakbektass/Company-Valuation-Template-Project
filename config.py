import os

tr_companies = ['Aksa Enerji','Odaş Elektrik','Ak Enerji','Migros','Carrefour SA',
                'BIM','Arcelik','Vestel','Bosch',]
sheet_names ={
    'Google': 'Google',
    'Apple': 'Apple',
    'Microsoft': 'Microsoft',
    'Coca-Cola':'Coca-Cola',
    'PepsiCo':'PepsiCo',
    'Monster': 'Monster',
    'Walmart':'Walmart',
    'Dollar General Corporation': 'Dollar General Corporation',
    'Target': 'Target',
    'Aksa Enerji': 'Aksa Enerji',
    'Odaş Elektrik':'Odaş Elektrik',
    'Ak Enerji': 'Ak Enerji',
    'Migros' :'Migros',
    'Carrefour SA': 'Carrefour SA',
    'BIM': 'BIM',
    'Arcelik': 'Arcelik',
    'Vestel': 'Vestel',
    'Bosch': 'Bosch'
}

excel_names = {
    'Google': os.path.join(os.path.dirname(__file__), 'financials', 'Google.xlsx'),
    'Apple': os.path.join(os.path.dirname(__file__), 'financials', 'Apple.xlsx'),
    'Microsoft': os.path.join(os.path.dirname(__file__), 'financials', 'Microsoft.xlsx'),
    'Coca-Cola': os.path.join(os.path.dirname(__file__), 'financials', 'Coca-Cola.xlsx'),
    'PepsiCo': os.path.join(os.path.dirname(__file__), 'financials', 'PepsiCo.xlsx'),
    'Monster': os.path.join(os.path.dirname(__file__), 'financials', 'Monster.xlsx'),
    'Walmart': os.path.join(os.path.dirname(__file__), 'financials', 'Walmart.xlsx'),
    'Dollar General Corporation': os.path.join(os.path.dirname(__file__), 'financials', 'Dollar.xlsx'),
    'Target': os.path.join(os.path.dirname(__file__), 'financials', 'Target.xlsx'),
    'Aksa Enerji': os.path.join(os.path.dirname(__file__), 'financials', 'Aksa Enerji.xlsx'),
    'Odaş Elektrik': os.path.join(os.path.dirname(__file__), 'financials', 'Odaş Elektrik.xlsx'),
    'Ak Enerji': os.path.join(os.path.dirname(__file__), 'financials', 'Ak Enerji.xlsx'),
    'Migros': os.path.join(os.path.dirname(__file__), 'financials', 'Migros.xlsx'),
    'Carrefour SA': os.path.join(os.path.dirname(__file__), 'financials', 'Carrefour SA.xlsx'),
    'BIM': os.path.join(os.path.dirname(__file__), 'financials', 'BIM.xlsx'),
    'Arcelik': os.path.join(os.path.dirname(__file__), 'financials', 'Arcelik.xlsx'),
    'Vestel': os.path.join(os.path.dirname(__file__), 'financials', 'Vestel.xlsx'),
    'Bosch': os.path.join(os.path.dirname(__file__), 'financials', 'Bosch.xlsx')
}

betas = {
    'Google': 1.12,
    'Apple': 1.2,
    'Microsoft': 0.94,
    'Coca-Cola':0.58,
    'PepsiCo':0.59,
    'Monster': 1.01,
    'Walmart':0.5,
    'Dollar General Corporation': 0.52,
    'Target': 0.95,
    'Aksa Enerji': 1.04,
    'Odaş Elektrik':1.48,
    'Ak Enerji': 1.07,
    'Migros' :1.08,
    'Carrefour SA': 1.05,
    'BIM': 0.51,
    'Arcelik': 0.84,
    'Vestel': 0.73,
    'Bosch': 0.82
}

no_of_common_stock={
    'Google': 658499.877,
    'Apple': 16185181,
    'Microsoft': 7479033.14,
    'Coca-Cola':4335028.73,
    'PepsiCo':1382683.56,
    'Monster': 529671.41,
    'Walmart':2752781.88,
    'Dollar General Corporation': 226997.02,
    'Target': 463696.41,
    'Aksa Enerji': 1226340,
    'Odaş Elektrik':1400000,
    'Ak Enerji': 729164,
    'Migros' :181054.23,
    'Carrefour SA': 127773.77,
    'BIM': 607200,
    'Arcelik': 675728.21,
    'Vestel': 335456.28,
    'Bosch': 2500
}

tickers = {
    'Google': "GOOGL",
    'Apple': "AAPL",
    'Microsoft': "MSFT",
    'Coca-Cola':"KO",
    'PepsiCo':"PEP",
    'Monster': "MUST",
    'Walmart':"WMT",
    'Dollar General Corporation': "DG",
    'Target': "TGT",
    'Aksa Enerji': "AKSEN.IS",
    'Odaş Elektrik':"ODAS.IS",
    'Ak Enerji': "AKENR.IS",
    'Migros' :"MGROS.IS",
    'Carrefour SA': "CRFSA.IS",
    'BIM': "BIMAS.IS",
    'Arcelik': "ARCLK.IS",
    'Vestel': "VESTL.IS",
    'Bosch': "BFREN.IS"
}


retail_us=['Walmart','Dollar General Corporation', 'Target']
drink_us=['Coca-Cola' ,'PepsiCo' , 'Monster' ]
tech_us=['Apple' , 'Microsoft' , 'Google']
electronic_tr=['Bosch' , 'Vestel' , 'Arcelik']
retail_tr=['Migros' , 'Carrefour SA' , 'BIM']
energy_tr=['Odaş Elektrik' , 'Ak Enerji' , 'Aksa Enerji']

sectors ={
    'Google': tech_us,
    'Apple': tech_us,
    'Microsoft': tech_us,
    'Coca-Cola':drink_us,
    'PepsiCo':drink_us,
    'Monster': drink_us,
    'Walmart':retail_us,
    'Dollar General Corporation': retail_us,
    'Target': retail_us,
    'Aksa Enerji': energy_tr,
    'Odaş Elektrik':energy_tr,
    'Ak Enerji': energy_tr,
    'Migros' :retail_tr,
    'Carrefour SA': retail_tr,
    'BIM': retail_tr,
    'Arcelik': electronic_tr,
    'Vestel': electronic_tr,
    'Bosch': electronic_tr
}
sectors_string ={
    'Google': 'Technology Sector in US',
    'Apple': 'Technology Sector in US',
    'Microsoft': 'Technology Sector in US',
    'Coca-Cola':'Drink Sector in US',
    'PepsiCo':'Drink Sector in US',
    'Monster': 'Drink Sector in US',
    'Walmart':'Retail Sector in US',
    'Dollar General Corporation': 'Retail Sector in US',
    'Target': 'Retail Sector in US',
    'Aksa Enerji': 'Energy Sector in Turkey',
    'Odaş Elektrik':'Energy Sector in Turkey',
    'Ak Enerji': 'Energy Sector in Turkey',
    'Migros' :'Retail Sector in Turkey',
    'Carrefour SA': 'Retail Sector in Turkey',
    'BIM': 'Retail Sector in Turkey',
    'Arcelik': 'Electronic Sector in Turkey',
    'Vestel': 'Electronic Sector in Turkey',
    'Bosch': 'Electronic Sector in Turkey'
}