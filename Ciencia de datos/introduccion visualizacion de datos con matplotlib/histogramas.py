import matplotlib.pyplot as plt

fig, ax = plt.subplot()
ax.hist(mens_rowing['Weight'])
ax.hist(mens_gymnastics['Weight'])
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('# of observations')
plt.legend()
plt.show()

#---------------------------------------------------------------------------------------------
fig, ax = plt.subplots()
ax.hist(mens_rowing['Weight'], label='Rowing', histtype='step', bins=5)
ax.hist(mens_gymnastics['Weight'], label='Gymnastics', histtype='step', bins=5)
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('# of observations')
ax.legend()
plt.show()

#----------------------------------------------------------------------------------------------
fig, ax = plt.subplot()
ax.bar('Rowing', mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())
ax.bar('Gymnastics', mens_gymnastics['Height'].mean(), yeer=mens_gymnastics['Height'].std())
ax.set_ylabel('Height (cm)')
plt.show()

#----------------------------------------------------------------------------------------------
fig, ax = plt.subplots()
ax.errorbar(seattle_weather['MONTH'],
            seattle_weather['MLY-TAVG-NORMAL'],
            yerr=seattle_weather['MLY-TAVG-STDDEV'])

ax.errorbar(austin_weather['MONTH'],
            austin_weather['MLY-TAVG-NORMAL'],
            yerr=austin_weather['MLY-TAVG-STDDEV'])

ax.set_ylabel('Temperature (Farenheit)')
plt.show()

#--------------------------------------------------------------------------------------------------
fig, ax = plt.subplots()
ax.boxplot([mens_rowing['Height'],
            mens_gymnastics['Height']])
ax.set_xticklabels(['Rowing','Gymnastics'])
ax.set_ylabel('Height (cm)')
plt.show()

#---------------------------------------------------------------------------------------------------
fig, ax = plt.subplots()

ax.scatter(climate_change['co2'], climate_change['relative_temp'])
ax.set_xlabel('CO2 (ppm)')
ax.set_ylabel('Relative temperature (C)')

plt.show()

#----------------------------------------------------------------------------------------------------
fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change['co2'], climate_change['relative_temp'], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel('CO2 (ppm)')

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel('Relative temperature (C)')

plt.show()
