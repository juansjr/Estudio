import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
ax.bar(medals.index, medals['Gold'])
ax.set_xticklabels(mendals.index, rotation=90)
ax.set_ylabel('Number of medals')
plt.show()
#-------------------------------------------------------------------------------------
ax.bar(medals.index, medals['Gold'], label='Gold')
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')
ax.bar(medals.index, medals['Bronze'],bottom=medals['Gold'] + medals['Silver'], label='Bronze')
ax.legend()
plt.show()
