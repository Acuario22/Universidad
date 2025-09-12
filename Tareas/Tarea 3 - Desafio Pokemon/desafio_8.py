import pandas as pd
from cargar_datos import df_pokemon

'''
8. Ejercicios de interpretación
-------------------------------
- Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones puedes sacar sobre los Pokémon de la primera generación?
- ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más especializado?
'''
#1.
#Tipos como Lucha, Dragón y Fuego tienen los promedios de Ataque más altos,
#por ende podemos decir que son tipos más ofensivos.
#Tipos como Roca, Tierra y Agua tienen Defensa más alta en promedio,
#por lo cual podemos decir que son tipos más defensivos.

#2.
#El coeficiente de correlación entre Ataque y Velocidad es 0.19,
#lo que indica que hay muy poca relación entre estas estadísticas,
#por ende tener un Pokémon rápido no implica que tenga un alto ataque.

#3.
#Los Pokémon tipo Bicho, Fantasma y Planta tienen los PS más homogéneos es decir baja desviación estándar,
#por ende podemos decir que son los tipos más balanceados en cuanto a vida.
#En cambio, los tipos Normal, Psiquico y Agua tienen PS más dispersos,
#lo que indica que dentro de estos tipos hay Pokémon con PS muy bajos y muy altos.

#4.
#Tipos como Hielo presentan valores de Ataque y Defensa similares,
#por lo cual podemos decir que son pokémones balanceados.
