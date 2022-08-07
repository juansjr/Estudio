#para guradar graficas en diferentes formatos se utiliza la sigiente linea de codigo.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

fig.savefig('Nombre.png', dpi=300)#se determina el nombre y el formato a guardar. El dpi sirve para determinar la calidad de la imagen.

# Para determinar el tamaño de la imagen utilizamos:
fig.set_size_inches([5,2])#Siendo el primer numero el ancho y el segundo el alto.

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals['Sport']==sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df['Weight'].mean(),
        yerr=sport_df['Weight'].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig('sports_weights.png')
plt.show()
