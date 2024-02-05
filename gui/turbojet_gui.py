import tkinter as tk
from tkinter import messagebox
from model.turbojet_model import TurbojetModel
from utils.calculations import calculate_thrust, calculate_fuel_flow

class TurbojetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Turbojet Engine Model")
        self.root.geometry("500x500")

        # Example GUI initialization code
        self.label_throttle = tk.Label(self.root, text="Throttle (0-1.0):")
        self.entry_throttle = tk.Entry(self.root)
        self.label_efficiency = tk.Label(self.root, text="Efficiency Factor (0-1.0):")
        self.entry_efficiency = tk.Entry(self.root)
        self.label_power = tk.Label(self.root, text="Power (kW):")
        self.entry_power = tk.Entry(self.root)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_and_display)

        self.output_label = tk.Label(self.root, text="Results will be displayed here.")

        # Place widgets using grid layout
        self.label_throttle.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_throttle.grid(row=0, column=1, padx=10, pady=5)
        self.label_efficiency.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_efficiency.grid(row=1, column=1, padx=10, pady=5)
        self.label_power.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_power.grid(row=2, column=1, padx=10, pady=5)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.output_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def calculate_and_display(self):
        # Get input values from the GUI
        throttle = float(self.entry_throttle.get()) if self.entry_throttle.get() else 0.0
        efficiency = float(self.entry_efficiency.get()) if self.entry_efficiency.get() else 0.0
        power = float(self.entry_power.get()) if self.entry_power.get() else 0.0

        # Use the TurbojetModel to perform calculations
        model = TurbojetModel()
        results = model.calculate({'throttle': throttle, 'efficiency': efficiency, 'power': power})

        # Display the results in the GUI with units
        self.output_label.config(text=f"Thrust: {results['Thrust']} kN, Fuel Flow: {results['Fuel Flow']} kg/s")

    def on_closing(self):
        if messagebox.askyesno(title="Exit Application", message="Are you sure you want to exit?"):
            self.root.destroy()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    gui = TurbojetGUI(root)
    root.mainloop()
