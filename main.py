import pandas as pd


columnas = ['target','ids','date','flag','user','text']
data = pd.read_csv('data/raw/data.csv', encoding = "latin-1", names=columnas)

data = data.sample(n=50000, random_state=42)
data = data.reset_index(drop=True) # reconstruimos los índices para que sean consecutivos
data.head()



from matplotlib import pyplot as plt
plt.hist(data['target'], bins=5)
