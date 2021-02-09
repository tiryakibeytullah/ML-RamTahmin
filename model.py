import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

first_ram = pd.read_excel('ram-verilerim.xlsx',sheet_name='Sheet1')
after_ram = pd.read_excel('ram-verilerim.xlsx',sheet_name='Sheet2')

first_ram = first_ram.iloc[:, 0:]
after_ram = after_ram.iloc[:, 0:]

GerekenKolonlar = ['Marka','Kapasite','Kategori','Fiyat']

print(first_ram)
print(after_ram)

first_ram = first_ram[GerekenKolonlar]
after_ram = after_ram[GerekenKolonlar]

print(first_ram.head(5))
print(after_ram.head(5))

bagimliDegisken = 'Fiyat'

X = after_ram[first_ram.columns.difference([bagimliDegisken])]
y = after_ram[[bagimliDegisken]]

print(X)
print(y)

LinearRegression = LinearRegression()
LinearRegression.fit(X,y)

joblib.dump(LinearRegression, 'ram-model.pkl')
print("Model Oluşturuldu.")

LinearRegression = joblib.load("ram-model.pkl")
modelKolonlari = list(X.columns)

joblib.dump(modelKolonlari,'ram-model-kolonlari.pkl')
print("Model Kolonları Oluşturuldu")
