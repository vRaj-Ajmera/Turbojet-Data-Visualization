import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import simpledialog, messagebox
from model.turbojet_model import TurbojetModel
from utils.unit_conversions import UnitConversions
import numpy as np

class TurbojetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Turbojet Engine Model")
        self.root.geometry("750x550")

        # Labels and Entries for input parameters
        self.label_M_0 = tk.Label(self.root, text="Low Inlet Mach Number:")
        self.entry_M_0 = tk.Entry(self.root, width=10)
        self.label_M_1 = tk.Label(self.root, text="High Inlet Mach Number:")
        self.entry_M_1 = tk.Entry(self.root, width=10)
        self.label_T_0 = tk.Label(self.root, text="Ambient Temperature:")
        self.entry_T_0 = tk.Entry(self.root, width=10)
        self.entry_T_0_unit = tk.StringVar()
        self.entry_T_0_unit.set("K")
        self.dropdown_T_0_unit = tk.OptionMenu(self.root, self.entry_T_0_unit, "K", "C", "F")
        self.label_P_0 = tk.Label(self.root, text="Ambient Pressure:")
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
        
        # Button to show altitude input
        self.altitude_button = tk.Button(self.root, text="Don't know values?", command=self.show_altitude_input)
        
        # Output label
        self.output_label = tk.Label(self.root, text="Results will be displayed here.")
        
        # Place widgets using grid layout
        # Your existing grid layout code
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
        self.altitude_button.grid(row=5, column=4, padx=10, pady=10, sticky=tk.W)  # New button added
        self.output_label.grid(row=6, column=0, columnspan=5, pady=10)

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

        # Convert ambient temperature to Kelvin based on the selected unit
        T_0_unit = self.entry_T_0_unit.get()
        if T_0_unit == "C":
            T_0 = UnitConversions.C_to_K(T_0)
        elif T_0_unit == "F":
            T_0 = UnitConversions.F_to_K(T_0)

        # Convert ambient pressure to kPa based on the selected unit
        P_0_unit = self.entry_P_0_unit.get()
        if P_0_unit == "Pa":
            P_0 = UnitConversions.Pa_to_kPa(P_0)
        elif P_0_unit == "atm":
            P_0 = UnitConversions.atm_to_kPa(P_0)

        # Convert turbine inlet temperature to Kelvin based on the selected unit
        T_t4_unit = self.entry_T_t4_unit.get()
        if T_t4_unit == "C":
            T_t4 = UnitConversions.C_to_K(T_t4)
        elif T_t4_unit == "F":
            T_t4 = UnitConversions.F_to_K(T_t4)

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
        plt.title('Calculated Thrust vs Inlet Mach Number')

        # Plot Mach number vs RPM
        plt.subplot(1, 2, 2)
        plt.plot(mach_vals, tsfc_vals)
        plt.xlabel('Mach Number')
        plt.ylabel('TSFC (kg kN$^{-1}$ hr$^{-1}$)')
        plt.title('Calculated TSFC vs Inlet Mach Number')

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
    
    def show_altitude_input(self):
        # Create a pop-up window
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Input Altitude")
        
        # Set size for the pop-up window
        popup_window.geometry("300x150")  # You can adjust the size as needed

        # Label and Entry for altitude input
        altitude_label = tk.Label(popup_window, text="Enter altitude:")
        altitude_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        altitude_entry = tk.Entry(popup_window, width=10)
        altitude_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Create a StringVar for the units and an OptionMenu
        units_var = tk.StringVar()
        units_var.set("km")  # Default unit
        units_dropdown = tk.OptionMenu(popup_window, units_var, "km", "m", "ft")
        units_dropdown.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        def calculate_and_display_values():
            # Retrieve altitude and units from the input fields
            altitude = float(altitude_entry.get())
            units = units_var.get()

            # Convert altitude to kilometers if necessary
            if units == "m":
                altitude = UnitConversions.meters_to_km(altitude)  # Convert from meters to km
            elif units == "ft":
                altitude = UnitConversions.feet_to_km(altitude)  # Convert from feet to km

            # Calculate ambient temperature and pressure based on altitude
            _, _, T, P, _, _ = self.AtmosphereFunction(altitude)

            # Display the calculated values in a message box
            message = f"Ambient Temperature: {T:.2f} K\nAmbient Pressure: {P:.2f} kPa"
            tk.messagebox.showinfo("Calculated Values", message)

        # Add a button to calculate and display values
        calculate_button = tk.Button(popup_window, text="Calculate", command=calculate_and_display_values)
        calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

        # Optional: Make the pop-up window modal to block interaction with the main window
        popup_window.transient(self.root)
        popup_window.grab_set()
        popup_window.wait_window()


    def AtmosphereFunction(self, h_G_km):       #Atmosphere Function input hieght in Kilometers
            h_G = h_G_km*3280.84              #Kilometers to feet
            r_e=3959*5280                     #miles to feet
            R=1716.5                          #ft2/R-sec
            g0=32.174                         #ft/s^2
            T0=518.69                         #deg R
            g_hG=g0*(r_e/(r_e+h_G))**2        #gravity acceleration based on geopotential altitude
            h=(r_e/(r_e+h_G))*h_G             #altitude from geopotential altitude and earth radius
            if h<36000:                       # standard atmosphere maths up until tropopause
                h0=0                          # initial altitude of comparison is sea level
                T0=518.69                     #deg R
                P0=2116.22                    #psf
                rho0=2.3769e-3                #slugs/ft3
                a1=-3.57/1000                 #deg R/ft
                T= T0 + a1*(h-h0)             # calculate temperature from linear distribution
                P= P0*(T/T0)**(-g0/(R*a1))    #pressure from temperature
                rho = rho0*(T/T0)**(-((g0/(R*a1))+1))       #density from temperature
            else:
                h0=36000                      #tropopause altitude (ft)
                P0=4.760119191888137e+2       #from anderson
                rho0=7.103559955456123e-4     #from running code at 36000
                T=389.99                      # constant temperature
                P= P0*np.exp((-g0/(R*T)*(h-h0)))            #pressure from temperature
                rho = rho0*np.exp(-(g0/(R*T)*(h-h0)))       #density from temperature
            a=np.sqrt(1.4*P/rho)              # speed of sound
            h_G = h_G_km/3280.84              #Feet to Km
            h = h/3280.84                     #Geopotential altitude in km
            T = T*0.555556                    #Rankine to Kelvin
            P = P /0.020885 /1000             #Psf to KPa
            rho = rho/515.4                   #Density in kg/m^2
            a = a/3.281                       #Local  m/s
            return [h_G, h, T, P, rho,a]


    def on_closing(self):
        if messagebox.askyesno(title="Exit Application", message="Are you sure you want to exit?"):
            self.root.destroy()

# Example usage
#if __name__ == "__main__":
#    root = tk.Tk()
#    gui = TurbojetGUI(root)
#    root.mainloop()
