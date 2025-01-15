import pandas as pd

carros = {
    'marca':['Fiat','Chevrolet','Ford'],
    'modelo':['Uno','Corsa','Fiesta'],
    'ano':['2010','2011','2012'],
}
dataframe = pd.DataFrame(carros)
dataframe.to_excel('./carros.xlsx')



