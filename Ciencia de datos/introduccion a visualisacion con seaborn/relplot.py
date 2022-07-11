#la funcion relplot es mas versatil por eso la seguiremos utilizando 
import seaborn as sns
import matplotlib.pyplot as plt

sns.relplot(x='acceleration', y='mpg',
            data=mpg,
            kind='scatter',
            style='origin',
            hue='origin')

plt.show()

#-------------------------------------------------------------------------------------------------
sns.relplot(x="absences", y="G3", 
                data=student_data,
                kind='scatter')

# Show plot
plt.show()
#-----------------------------------------------------------------------------------------------