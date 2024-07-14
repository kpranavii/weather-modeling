import matplotlib.pyplot as plt
import numpy as np

def quadratic_sol(t):
  #assuming coefficients
  a = 0.1
  b = -1
  c = 10

  temperature = a*t**2 + b*t + c
  return temperature

def main():
  time = np.linspace(0,72)
  precipitation= quadratic_sol(time)
  plt.plot(time, precipitation, label='Hard-coded variables')
  plt.xlabel('Time(in hour)')
  plt.ylabel('Precipitation(in mm)')
  plt.legend()
  plt.title('Weather Modeling with quadratic solution (hard-coded variables)')

  plt.show()

if __name__ == '__main__':
  main()