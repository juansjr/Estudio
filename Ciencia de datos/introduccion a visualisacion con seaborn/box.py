import seaborn as sns
import matplotlib.pyplot as plt

# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet', y='G3',
            data=student_data,
            kind='box',
            col='location',
            hue='location',
            sym='')





# Show plot
plt.show()

#-----------------------------------------------------------------------------------------

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()