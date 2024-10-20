import numpy as np
import pandas as pd

daten = {
    'Name': ['Max', 'Peter', 'Julia', 'Andrea'],
    'Alter': [25, 30, 35, 40],
    'Stadt': ['Berlin', 'Hamburg', 'München', 'Köln']
}

df = pd.DataFrame(daten)
print(df)