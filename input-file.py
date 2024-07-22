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