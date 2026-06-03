import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')   # Use non-interactive backend — safe for all environments
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401

# ============================================================
# EXPERIMENT 6: 3D and Multi-variable Visualization
# Subject: AI in Mechanical Engineering (ONT406)
# Sharda University
# ============================================================

class DatasetError(ValueError):
    """Raised when dataset parameters are invalid."""
    pass

class PlotError(RuntimeError):
    """Raised when a plot cannot be generated."""
    pass

# -------------------------------------------------------
# Input Helpers
# -------------------------------------------------------
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("  Error: Enter a numeric value.")
            continue
        if value <= 0:
            print("  Error: Value must be greater than zero.")
            continue
        return value

def get_positive_int(prompt, minimum=10):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Error: Enter a whole number.")
            continue
        if value < minimum:
            print(f"  Error: Value must be at least {minimum}.")
            continue
        return value

def get_range(label, must_positive=False):
    """Get a validated min-max range."""
    while True:
        try:
            low  = float(input(f"  {label} min: "))
            high = float(input(f"  {label} max: "))
        except ValueError:
            print("  Error: Enter numeric values.")
            continue
        if must_positive and low <= 0:
            print("  Error: Minimum must be positive.")
            continue
        if high <= low:
            print("  Error: Maximum must be greater than minimum.")
            continue
        return low, high

# -------------------------------------------------------
# Dataset Builders
# -------------------------------------------------------
def generate_dataset(n, temp_r, pres_r, vol_r, rpm_r, vib_r):
    """Generate a thermodynamic dataset with given ranges."""
    if n < 10:
        raise DatasetError("Need at least 10 samples.")
    for label, (lo, hi) in [
        ("Temperature", temp_r), ("Pressure", pres_r),
        ("Volume", vol_r),       ("RPM", rpm_r),
        ("Vibration", vib_r)
    ]:
        if hi <= lo:
            raise DatasetError(f"{label}: max must be greater than min.")

    np.random.seed(0)
    return pd.DataFrame({
        "Temperature": np.random.uniform(*temp_r, n),
        "Pressure":    np.random.uniform(*pres_r, n),
        "Volume":      np.random.uniform(*vol_r,  n),
        "RPM":         np.random.uniform(*rpm_r,  n),
        "Vibration":   np.random.uniform(*vib_r,  n),
    })

def preset_dataset():
    return generate_dataset(
        100,
        temp_r=(300, 800), pres_r=(1, 10),
        vol_r=(0.1, 2.0),  rpm_r=(1000, 5000),
        vib_r=(0.5, 3.5)
    )

# -------------------------------------------------------
# Plot Functions
# -------------------------------------------------------
def plot_3d(data, filename="3d_thermodynamic_plot.png"):
    """3D scatter plot of Temperature-Pressure-Volume."""
    try:
        fig = plt.figure(figsize=(9, 7))
        ax  = fig.add_subplot(111, projection="3d")
        sc  = ax.scatter(
            data["Volume"], data["Pressure"], data["Temperature"],
            c=data["Temperature"], cmap="hot", alpha=0.8
        )
        ax.set_xlabel("Volume (m³)")
        ax.set_ylabel("Pressure (bar)")
        ax.set_zlabel("Temperature (K)")
        ax.set_title("3D Thermodynamic Relationship (P-V-T)")
        plt.colorbar(sc, label="Temperature (K)", shrink=0.5, ax=ax)
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.close()
        print(f"  ✓ 3D plot saved: {filename}")
    except (KeyError, TypeError) as e:
        raise PlotError(f"3D plot failed — missing or invalid column: {e}")
    except OSError as e:
        raise PlotError(f"Could not save plot file: {e}")

def plot_heatmap(data, filename="correlation_heatmap.png"):
    """Correlation heatmap of all variables."""
    try:
        corr = data.corr(numeric_only=True)
        if corr.empty:
            raise PlotError("No numeric columns for correlation.")
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            corr, annot=True, cmap="coolwarm",
            fmt=".2f", linewidths=0.5, square=True
        )
        plt.title("Correlation Heatmap of Mechanical Parameters")
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.close()
        print(f"  ✓ Heatmap saved: {filename}")
        print("\n  Correlation Matrix:")
        print(corr.round(2).to_string())
    except (KeyError, TypeError) as e:
        raise PlotError(f"Heatmap failed: {e}")
    except OSError as e:
        raise PlotError(f"Could not save heatmap: {e}")

def plot_histogram(data, threshold, filename="vibration_histogram.png"):
    """Vibration histogram with fault threshold line."""
    if "Vibration" not in data.columns:
        raise PlotError("Dataset has no 'Vibration' column.")
    if threshold <= 0:
        raise PlotError("Threshold must be positive.")
    try:
        fault_count = int((data["Vibration"] > threshold).sum())
        plt.figure(figsize=(8, 5))
        plt.hist(
            data["Vibration"], bins=15,
            color="steelblue", edgecolor="black", alpha=0.8
        )
        plt.axvline(
            x=threshold, color="red", linestyle="--",
            linewidth=2, label=f"Fault Threshold ({threshold}g)"
        )
        plt.xlabel("Vibration Amplitude (g)")
        plt.ylabel("Frequency")
        plt.title(f"Vibration Distribution  |  Faults: {fault_count}")
        plt.legend()
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.close()
        print(f"  ✓ Histogram saved: {filename}")
        print(f"  Fault events (>{threshold}g): {fault_count}")
    except (TypeError, KeyError) as e:
        raise PlotError(f"Histogram failed: {e}")
    except OSError as e:
        raise PlotError(f"Could not save histogram: {e}")

# -------------------------------------------------------
# Main Program
# -------------------------------------------------------
def main():
    print("=" * 55)
    print("   EXPERIMENT 06: 3D Visualization (Matplotlib/Seaborn)")
    print("   AI in Mechanical Engineering — ONT406")
    print("   Sharda University")
    print("=" * 55)

    data = None

    while True:
        print("\n--- MENU ---")
        print("1. Load Preset Dataset")
        print("2. Create Custom Dataset")
        print("3. Plot 3D Scatter (T-P-V)")
        print("4. Plot Correlation Heatmap")
        print("5. Plot Vibration Histogram")
        print("6. Plot All Three")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice in ["3", "4", "5", "6"] and data is None:
            print("  Error: Load a dataset first (option 1 or 2).")
            continue

        if choice == "1":
            try:
                data = preset_dataset()
                print(f"  ✓ Preset dataset loaded: {len(data)} samples.")
            except DatasetError as e:
                print(f"  Dataset Error: {e}")

        elif choice == "2":
            try:
                print("\n  --- Custom Dataset ---")
                n      = get_positive_int("  Number of samples (min 10): ", minimum=10)
                print("  Temperature range (K):")
                temp_r = get_range("  Temperature", must_positive=True)
                print("  Pressure range (bar):")
                pres_r = get_range("  Pressure",    must_positive=True)
                print("  Volume range (m³):")
                vol_r  = get_range("  Volume",      must_positive=True)
                print("  RPM range:")
                rpm_r  = get_range("  RPM",         must_positive=True)
                print("  Vibration range (g):")
                vib_r  = get_range("  Vibration",   must_positive=True)
                data   = generate_dataset(n, temp_r, pres_r, vol_r, rpm_r, vib_r)
                print(f"  ✓ Custom dataset created: {len(data)} samples.")
            except DatasetError as e:
                print(f"  Dataset Error: {e}")

        elif choice == "3":
            try:
                plot_3d(data)
            except PlotError as e:
                print(f"  Plot Error: {e}")

        elif choice == "4":
            try:
                plot_heatmap(data)
            except PlotError as e:
                print(f"  Plot Error: {e}")

        elif choice == "5":
            try:
                threshold = get_positive_float("  Fault threshold (g): ")
                plot_histogram(data, threshold)
            except PlotError as e:
                print(f"  Plot Error: {e}")

        elif choice == "6":
            try:
                threshold = get_positive_float("  Fault threshold (g): ")
                plot_3d(data)
                plot_heatmap(data)
                plot_histogram(data, threshold)
                print("  ✓ All three plots saved successfully.")
            except PlotError as e:
                print(f"  Plot Error: {e}")

        elif choice == "7":
            print("\nExiting. Goodbye!")
            break

        else:
            print("  Error: Invalid choice. Please enter 1 through 7.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Program interrupted by user. Goodbye!")
