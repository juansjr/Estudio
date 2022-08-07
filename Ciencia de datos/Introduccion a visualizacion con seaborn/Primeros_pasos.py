import matplotlib.pyplot as plt
import seaborn as sns


height = [62, 64, 69, 75, 66, 68, 65, 71, 76, 73]
weight = [120, 136, 148, 175, 137,165, 154, 172, 200, 187]

sns.scatterplot(x=height, y=weight)
plt.show()
#----------------------------------------------------------------------------------------
sns.countplot(y=region)
plt.show()