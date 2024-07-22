import matplotlib.pyplot as plt
import numpy as np

# to calculate precipitation
def calculate_precipitation(temperature, humidity,pressure):
    # Coefficients
    a = 0.01 
    b = -0.6
    c = 0.2
    
    precipitation = a * humidity**2 + b * temperature + c* pressure
    return max(0, precipitation)  # non negative value for precipitation

humidity_range = [] # Humidity range from 0% to 100%
set=[] #input set
while(True):
    temperature = float(input("Enter temperature value(in ℃)"))
    pressure= float(input("Enter pressure value(in mmHg)"))
    humidity=float(input("Enter humidity value(in %)"))
    set.append([temperature,pressure,humidity])
    if(input("Exit?(y/n):")).lower()=="y":
        break
precipitation_values=[]
for i, set in enumerate(set):
    temperature,pressure,humidity=set
    humidity_range.append(humidity)
    p=calculate_precipitation(temperature, humidity,pressure)
    precipitation_values.append(p)
    print("Precipitation for",i+1,": ",p,"mm")

plt.plot(humidity_range, precipitation_values)
plt.xlabel('Humidity (%)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Humidity and Precipitation')
plt.grid(True)
plt.show()
