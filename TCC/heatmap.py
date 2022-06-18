print('CRIANDO UM MAPA DE CALOR')

import numpy as np 
import seaborn as sns 
import matplotlib.pylab as plt

i = 0
sensor = []

# Simulando os dados dos sensores
while i < 10:
    dados = np.random.uniform(low=0, high=1, size=20).tolist()
    sensor.append(dados)
    i += 1

# Nomeando os eixos
x = [f'Sensor {n}' for n in range(1,21)]
y = [f'{t}s' for t in range(1,11)]

# Gerando o Mapa de calor
mapa = sns.heatmap(sensor , linewidth = 0.5 , cmap = 'coolwarm', xticklabels=x, yticklabels=y) 

# seaborn.heatmap (data, *, vmin = None, vmax = None, cmap = None, center = None, robust = False, annot = None, fmt = '. 2g', annot_kws = None, linewidths = 0, linecolor = 'branco', cbar = Verdadeiro, cbar_kws = Nenhum, cbar_ax = Nenhum, quadrado = Falso, xticklabels = 'auto', yticklabels = 'auto', máscara = Nenhum, ax = Nenhum, ** kwargs)

plt.title('Mapa de calor') 
plt.show() 