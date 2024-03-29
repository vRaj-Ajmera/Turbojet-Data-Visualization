import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox
from model.turbojet_model import TurbojetModel

class TurbojetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Turbojet Engine Model")
        self.root.geometry("750x550")

        # Labels and Entries for input parameters
        self.label_M_0 = tk.Label(self.root, text="Low Mach Number:")
        self.entry_M_0 = tk.Entry(self.root, width=10)
        self.label_M_1 = tk.Label(self.root, text="High Mach Number:")
        self.entry_M_1 = tk.Entry(self.root, width=10)
        self.label_T_0 = tk.Label(self.root, text="Total Temperature:")
        self.entry_T_0 = tk.Entry(self.root, width=10)
        self.entry_T_0_unit = tk.StringVar()
        self.entry_T_0_unit.set("K")
        self.dropdown_T_0_unit = tk.OptionMenu(self.root, self.entry_T_0_unit, "K", "C", "F")
        self.label_P_0 = tk.Label(self.root, text="Total Pressure:")
        self.entry_P_0 = tk.Entry(self.root, width=10)
        self.entry_P_0_unit = tk.StringVar()
        self.entry_P_0_unit.set("kPa")
        self.dropdown_P_0_unit = tk.OptionMenu(self.root, self.entry_P_0_unit, "kPa", "Pa", "atm")
        self.label_T_t4 = tk.Label(self.root, text="Turbine Inlet Temperature:")
        self.entry_T_t4 = tk.Entry(self.root, width=10)
        self.entry_T_t4_unit = tk.StringVar()
        self.entry_T_t4_unit.set("K")
        self.dropdown_T_t4_unit = tk.OptionMenu(self.root, self.entry_T_t4_unit, "K", "C", "F")
        self.label_P9rat = tk.Label(self.root, text="Exit Pressure Ratio:")
        self.entry_P9rat = tk.Entry(self.root, width=10)

        # Button to trigger calculation and plotting
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_and_display)

        # Button to clear calculation text boxes (Clear Inputs)
        self.clear_button = tk.Button(self.root, text="Clear Inputs", command=self.clear_inputs)

        # Button to fill default values in the empty boxes (Use Default Inputs)
        self.default_button = tk.Button(self.root, text="Use Default Inputs", command=self.fill_default_inputs)

        # Output label
        self.output_label = tk.Label(self.root, text="Results will be displayed here.")

        # Place widgets using grid layout
        self.label_M_0.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_M_0.grid(row=0, column=1, padx=5, pady=5)
        self.label_M_1.grid(row=0, column=2, padx=10, pady=5, sticky=tk.E)
        self.entry_M_1.grid(row=0, column=3, padx=5, pady=5)
        self.label_T_0.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_T_0.grid(row=1, column=1, padx=5, pady=5)
        self.dropdown_T_0_unit.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        self.label_P_0.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_P_0.grid(row=2, column=1, padx=5, pady=5)
        self.dropdown_P_0_unit.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
        self.label_T_t4.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_T_t4.grid(row=3, column=1, padx=5, pady=5)
        self.dropdown_T_t4_unit.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
        self.label_P9rat.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_P9rat.grid(row=4, column=1, padx=5, pady=5)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.clear_button.grid(row=5, column=2, pady=10)
        self.default_button.grid(row=5, column=3, pady=10)
        self.output_label.grid(row=6, column=0, columnspan=4, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def calculate_and_display(self):
        self.fill_default_inputs()

        # Retrieve input values from the GUI after filling default values
        M_0 = float(self.entry_M_0.get())
        M_1 = float(self.entry_M_1.get())
        T_0 = float(self.entry_T_0.get())
        P_0 = float(self.entry_P_0.get())
        T_t4 = float(self.entry_T_t4.get())
        P9rat = float(self.entry_P9rat.get())

        # Calculate results
        inputs = {'M_0': M_0, 'M_1': M_1, 'T_0': T_0, 'P_0': P_0, 'T_t4': T_t4, 'P9rat': P9rat}
        model = TurbojetModel(**inputs)
        mach_vals, thrust_vals, tsfc_vals = model.calculate()

        # Plotting
        plt.figure(figsize=(12, 6))

        # Plot Mach number vs Thrust
        plt.subplot(1, 2, 1)
        plt.plot(mach_vals, thrust_vals)
        plt.xlabel('Mach Number')
        plt.ylabel('Thrust (N)')
        plt.title('Thrust vs Mach Number')

        # Plot Mach number vs RPM
        plt.subplot(1, 2, 2)
        plt.plot(mach_vals, tsfc_vals)
        plt.xlabel('Mach Number')
        plt.ylabel('TSFC (kg kN$^{-1}$ hr$^{-1}$)')
        plt.title('Thrust Specific Fuel Consumption vs Mach Number')

        plt.tight_layout()
        plt.show()

    def clear_inputs(self):
        # Clear all input fields
        self.entry_M_0.delete(0, tk.END)
        self.entry_M_1.delete(0, tk.END)
        self.entry_T_0.delete(0, tk.END)
        self.entry_P_0.delete(0, tk.END)
        self.entry_T_t4.delete(0, tk.END)
        self.entry_P9rat.delete(0, tk.END)

    def fill_default_inputs(self):
        # Fill empty input fields with default values and set corresponding dropdowns to default units
        if not self.entry_M_0.get():
            self.entry_M_0.insert(tk.END, "0.0")
        if not self.entry_M_1.get():
            self.entry_M_1.insert(tk.END, "2.0")
        if not self.entry_T_0.get():
            self.entry_T_0.insert(tk.END, "229.8")
            self.entry_T_0_unit.set("K")
        if not self.entry_P_0.get():
            self.entry_P_0.insert(tk.END, "30.8")
            self.entry_P_0_unit.set("kPa")
        if not self.entry_T_t4.get():
            self.entry_T_t4.insert(tk.END, "1670")
            self.entry_T_t4_unit.set("K")
        if not self.entry_P9rat.get():
            self.entry_P9rat.insert(tk.END, "0.955")

    def on_closing(self):
        if messagebox.askyesno(title="Exit Application", message="Are you sure you want to exit?"):
            self.root.destroy()

# Example usage
#if __name__ == "__main__":
#    root = tk.Tk()
#    gui = TurbojetGUI(root)
#    root.mainloop()
