import matplotlib.pyplot as plt
import numpy as np

# to calculate precipitation
def calculate_precipitation(temperature, humidity,pressure):
    # Coefficients
    a = 0.01 
    b = -0.6
    c = 0.2*pressure
    
    precipitation = a * humidity**2 + b * temperature + c
    return max(0, precipitation)  # non negative value for precipitation

humidity_range = np.linspace(0, 100, 100)  # Humidity range from 0% to 100%
temperature = 21.0  # temperature value
pressure= 600.0 #pressure value

# Calculate precipitation for each humidity in the range
precipitation_values = [calculate_precipitation(temperature, hum,pressure) for hum in humidity_range]

plt.plot(humidity_range, precipitation_values)
plt.xlabel('Humidity (%)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Humidity and Precipitation')
plt.grid(True)
plt.legend()
plt.show()
