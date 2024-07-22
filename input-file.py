import matplotlib.pyplot as plt
import pandas as pd

# to calculate precipitation
def calculate_precipitation(temperature, humidity,pressure):
    # Coefficients
    a = 0.01 
    b = -0.6
    c = 0.2*pressure
    
    precipitation = a * humidity**2 + b * temperature + c
    return max(0, precipitation)  # non negative value for precipitation

df= pd.read_csv('data.csv')
temperature=[]
humidity=[]
pressure=[]
for index, row in df.iterrows():
    temperature.append(row['Temperature'])
    humidity.append(row['Humidity'])
    pressure.append(row['Pressure'])
precipitation_values=[]
for i in range(0,6):
    precipitation_values.append(calculate_precipitation(temperature[i], humidity[i],pressure[i]))

plt.plot(humidity, precipitation_values)
plt.xlabel('Humidity (%)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Humidity and Precipitation')
plt.grid(True)
plt.show()
