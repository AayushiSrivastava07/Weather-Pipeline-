import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

print(df.head())

# Temperature Trend Graph
plt.figure(figsize=(10, 5))

plt.plot(df["temperature"])

plt.xlabel("Records")
plt.ylabel("Temperature")
plt.title("Temperature Trend Analysis")

plt.show()
