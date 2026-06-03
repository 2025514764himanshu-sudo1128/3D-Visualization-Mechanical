# Experiment 06 — Code Explanation
# 3D and Multi-variable Visualization of Mechanical Trends

---

## What is this program doing?

Engineers need to understand how multiple variables
relate to each other simultaneously. This program:

1. Creates a thermodynamic dataset (Temperature, Pressure, Volume, RPM, Vibration)
2. Plots a 3D scatter plot to visualize P-V-T relationship
3. Creates a heatmap showing which variables are correlated
4. Plots a histogram of vibration distribution
5. Saves all plots as PNG image files

---

## Line by Line Explanation

---

### Lines 1-5 (Imports)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
```
**matplotlib.pyplot:** The main plotting library.
`plt` is the universal short name.
Handles all 2D plots: line, bar, scatter, histogram.

**seaborn:** Built on matplotlib, makes statistical plots
easier and more beautiful. Used for heatmaps, pair plots.

**mpl_toolkits.mplot3d:** Extension for 3D plotting.
Must be imported specifically for 3D plots.
`Axes3D` is the 3D plotting object.

---

### Lines 8-15 (Generate Dataset)
```python
np.random.seed(0)
data = pd.DataFrame({
    "Temperature": np.random.uniform(300, 800, 100),
    "Pressure":    np.random.uniform(1, 10, 100),
    "Volume":      np.random.uniform(0.1, 2.0, 100),
    "RPM":         np.random.uniform(1000, 5000, 100),
    "Vibration":   np.random.uniform(0.5, 3.5, 100)
})
```
**np.random.uniform(low, high, size):**
Generates random numbers uniformly distributed between low and high.
Unlike normal distribution, all values are equally likely.

**Why 5 variables?**
Real machines have many sensors reading simultaneously.
Visualization helps find which variables are related.

---

### Lines 18-28 (3D Scatter Plot)
```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    data["Volume"],
    data["Pressure"],
    data["Temperature"],
    c=data["Temperature"],
    cmap='hot'
)
ax.set_xlabel("Volume (m³)")
ax.set_ylabel("Pressure (bar)")
ax.set_zlabel("Temperature (K)")
```
**plt.figure(figsize=(8,6)):**
Creates a new figure canvas. figsize=(width, height) in inches.

**fig.add_subplot(111, projection='3d'):**
- `111` means: 1 row, 1 column, 1st subplot (the only one)
- `projection='3d'` activates 3D mode

**ax.scatter(x, y, z):**
Plots points in 3D space.
Each point represents one data row.

**c=data["Temperature"], cmap='hot':**
Colors each point by Temperature value.
`cmap='hot'` = color scale from black→red→yellow→white
(cool = dark, hot = bright). Visual, intuitive!

**plt.colorbar():**
Adds the color legend showing what each color means.

**plt.savefig("filename.png"):**
Saves the plot as an image file.
You can then add this image to your GitHub repo!

---

### Lines 31-36 (Correlation Heatmap)
```python
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
```
**data.corr():**
Calculates the **Pearson correlation coefficient** between
every pair of columns.
Result is a 5×5 matrix showing all correlations.

**Correlation values:**
- +1.0 → Perfect positive correlation (one goes up, other goes up)
- -1.0 → Perfect negative correlation (one goes up, other goes down)
- 0.0 → No correlation (completely independent)

**sns.heatmap():**
Visualizes the correlation matrix as colored grid.

Parameters:
- `annot=True` → Show the number inside each cell
- `cmap='coolwarm'` → Blue=negative, Red=positive, White=zero
- `fmt=".2f"` → Format numbers to 2 decimal places

**Why use a heatmap?**
A 5×5 table of numbers is hard to read.
Colors immediately show strong vs weak correlations at a glance.

---

### Lines 39-47 (Vibration Histogram)
```python
plt.hist(data["Vibration"], bins=10, color='steelblue', edgecolor='black')
plt.axvline(x=2.5, color='red', linestyle='--', label='Fault Threshold')
```
**plt.hist():**
Plots a histogram — counts how many values fall in each range.

Parameters:
- `bins=10` → Divide range into 10 equal intervals
- `color='steelblue'` → Fill color
- `edgecolor='black'` → Border color of each bar

**plt.axvline():**
Draws a vertical line at x=2.5 (the fault threshold).
`linestyle='--'` = dashed line
`color='red'` = red color

**What histogram shows:**
Most vibration values are between 0.5-3.5g.
The red line at 2.5g shows where faults start.
Bars to the right of red line = fault events.

---

### Lines 50-51 (Saving and Showing)
```python
plt.savefig("vibration_histogram.png")
plt.show()
```
**plt.savefig():**
MUST be called BEFORE plt.show() — otherwise saves blank.
Saves the current figure to disk as PNG.

**plt.show():**
Displays the plot on screen in a popup window.
On servers/terminals without display, this can be skipped.

---

## Visualization Types Summary

| Plot Type | Function | Use Case |
|---|---|---|
| 3D Scatter | ax.scatter() with projection='3d' | 3 variable relationships |
| Heatmap | sns.heatmap() | Correlation between many variables |
| Histogram | plt.hist() | Frequency distribution of one variable |
| Line plot | plt.plot() | Trends over time |
| Scatter | plt.scatter() | 2 variable relationships |

## Correlation vs Causation

**Important:** Correlation does NOT mean causation!
Two variables can be correlated by coincidence or
because both are caused by a third variable.
Engineering judgment is needed to interpret correlations.
