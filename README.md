# Experiment 06: 3D and Multi-variable Visualization of Mechanical Trends

---

## Aim
To visualize multi-dimensional trends (Temperature vs Pressure vs Volume) using Matplotlib and Seaborn.

---

## Concepts Covered
- 3D scatter plots using mpl_toolkits
- Correlation matrix analysis
- Heatmap visualization using Seaborn
- Histogram for frequency distribution
- Saving plots as PNG files

---

## Software Required

| Software | Purpose | Download Link |
|---|---|---|
| Python 3.x | Programming language | https://www.python.org/downloads/ |
| VS Code | Code editor | https://code.visualstudio.com/ |
| Git | Version control | https://git-scm.com/ |

---

## Installation Steps

### Step 1: Install Python
```
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or above
3. CHECK "Add Python to PATH"
4. Verify: python --version
```

### Step 2: Install Required Libraries
```bash
pip install numpy pandas matplotlib seaborn
```

### Step 3: Verify Installation
```bash
python -c "import matplotlib; print('Matplotlib:', matplotlib.__version__)"
python -c "import seaborn; print('Seaborn:', seaborn.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"
```

### Step 4: Install Jupyter (Optional but Recommended for Plots)
```bash
pip install jupyter
jupyter notebook
```

---

## How to Run

```bash
git clone https://github.com/2025514764himanshu-sudo1128/3D-Visualization-Mechanical.git
cd 3D-Visualization-Mechanical
python mechanical_visualization.py
```

---

## Output Files Generated
```
3d_thermodynamic_plot.png   - 3D scatter plot of P-V-T relationship
correlation_heatmap.png     - Heatmap of variable correlations
vibration_histogram.png     - Distribution of vibration amplitudes
```

---

## Expected Console Output
```
3D plot saved as: 3d_thermodynamic_plot.png
Heatmap saved as: correlation_heatmap.png
Histogram saved as: vibration_histogram.png

=== Correlation Matrix ===
             Temperature  Pressure  Volume   RPM  Vibration
Temperature         1.00      0.03    0.02  0.01      -0.02
Pressure            0.03      1.00    0.08 -0.08       0.05
...
```

---

## Author
**Himanshu Kumar** (2025514764)
Department of Electrical, Electronics and Communication Engineering
Sharda University, Greater Noida
