# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x='model_year', y='mpg',
            data=mpg,
            kind='line')


# Show plot
plt.show()
#-------------------------------------------------------------------------------------------------

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",
            ci='sd')

# Show plot
plt.show()

#-------------------------------------------------------------------------------------------------

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year', y='horsepower',
            data=mpg,
            kind='line',
            ci=None)



# Show plot
plt.show()

#-------------------------------------------------------------------------------------------------
