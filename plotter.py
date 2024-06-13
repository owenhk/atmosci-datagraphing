import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.ticker import MaxNLocator
import matplotlib.colors  as mcolors

import os
from dotenv import load_dotenv
load_dotenv()

path_to_csv = os.environ.get("CSV_LOCATION")
download_graph_to = os.environ.get("SAVE_LOCATION")
data = pd.read_csv(path_to_csv)
# Create the scatter plot
plt.figure(figsize=(10, 6))


# Calculate the median (Q2) of the filtered temperature data
midpoint = int(os.environ.get("MIDPOINT"))
print(midpoint)
vmax = max(data["Temperature"])
vmin = min(data["Temperature"])

print(max(data["Temperature"]))
print(min(data["Temperature"]))
print(vmax)
print(vmin)

fig, ax = plt.subplots(figsize=(10, 6))

norm = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=midpoint, vmax=vmax)
scatter = ax.scatter(data['Time'], data['Altitude'], c=data['Temperature'], cmap='coolwarm', norm=norm)

# Adding colorbar, labels, and title
plt.colorbar(scatter, label='Temperature (°C)')
plt.xlabel('Time (PDT)')
plt.ylabel('Altitude (Meters)')
plt.title('Effect of Altitude (m) on Temperature (C°)')
plt.suptitle("Measured using infared ambient temperature sensor and GPS sensor")

# Customizing x-axis to display a maximum of 4 labels
ax = plt.gca()  # Get the current axis
ax.xaxis.set_major_locator(MaxNLocator(4))  # Set the maximum number of ticks on the x-axis

# Rotate date labels for better readability
plt.gcf().autofmt_xdate()

# Save the figure
plt.savefig(download_graph_to, dpi=500)  # Save as 4K image

