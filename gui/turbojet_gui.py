import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox
from model.turbojet_model import TurbojetModel
from utils.unit_conversions import UnitConversions

class TurbojetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Turbojet Engine Model")
        self.root.geometry("700x550")

        # Example GUI initialization code
        self.label_throttle = tk.Label(self.root, text="Throttle (0-1.0):")
        self.entry_throttle = tk.Entry(self.root)
        self.label_efficiency = tk.Label(self.root, text="Efficiency Factor (0-1.0):")
        self.entry_efficiency = tk.Entry(self.root)
        self.label_power = tk.Label(self.root, text="Power (kW):")
        self.entry_power = tk.Entry(self.root)

        self.label_altitude_range = tk.Label(self.root, text="Altitude Range:")
        self.entry_altitude_min = tk.Entry(self.root)
        self.entry_altitude_max = tk.Entry(self.root)
        self.altitude_unit = tk.StringVar(self.root)
        self.altitude_unit.set("Feet")  # Default unit selection
        self.altitude_unit_menu = tk.OptionMenu(self.root, self.altitude_unit, "Feet", "Meters")

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_and_display)

        self.output_label = tk.Label(self.root, text="Results will be displayed here.")

        # Place widgets using grid layout
        self.label_throttle.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_throttle.grid(row=0, column=1, padx=10, pady=5)
        self.label_efficiency.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_efficiency.grid(row=1, column=1, padx=10, pady=5)
        self.label_power.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_power.grid(row=2, column=1, padx=10, pady=5)
        self.label_altitude_range.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_altitude_min.grid(row=3, column=1, padx=5, pady=5)
        self.entry_altitude_max.grid(row=3, column=2, padx=5, pady=5)
        self.altitude_unit_menu.grid(row=3, column=3, padx=5, pady=5)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.output_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def calculate_and_display(self):
        # Get input values from the GUI
        throttle = float(self.entry_throttle.get()) if self.entry_throttle.get() else 0.0
        efficiency = float(self.entry_efficiency.get()) if self.entry_efficiency.get() else 0.0
        power = float(self.entry_power.get()) if self.entry_power.get() else 0.0
        altitude_min = float(self.entry_altitude_min.get()) if self.entry_altitude_min.get() else 0.0
        altitude_max = float(self.entry_altitude_max.get()) if self.entry_altitude_max.get() else 0.0
        altitude_unit = self.altitude_unit.get()

        # Convert altitude to feet if in meters
        #if altitude_unit == "Meters":
            #altitude_min = UnitConversions.meters_to_feet(altitude_min)
            #altitude_max = UnitConversions.meters_to_feet(altitude_max)

        # Generate altitude range
        altitude_range = range(int(altitude_min), int(altitude_max) + 1)

        # Calculate mass flow at each altitude point
        model = TurbojetModel()
        results = model.calculate({'throttle': throttle, 'efficiency': efficiency, 'power': power})
        mass_flows = [results['Fuel Flow']] * len(altitude_range)

        # Plot mass flow vs altitude
        plt.plot(altitude_range, mass_flows)
        plt.xlabel('Altitude (meters)' if altitude_unit == 'Meters' else 'Altitude (feet)')
        plt.ylabel('Mass Flow (kg/s)')
        plt.title('Mass Flow vs Altitude')
        plt.grid(True)
        plt.show()

    def on_closing(self):
        if messagebox.askyesno(title="Exit Application", message="Are you sure you want to exit?"):
            self.root.destroy()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    gui = TurbojetGUI(root)
    root.mainloop()
