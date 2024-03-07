# turbine_model.py
pip install cantera
import cantera as ct
class TurbineModel:
    """
    Class for modeling turbine behavior.
    """

def TVel2h_total(t, v):
    """
    Calculate the enthalpy of air at given temperature and pressure.

    Parameters:
        t (float): The temperature in Kelvin.
        v (float): The air velocity magnitude in m/s.

    Returns:
        float: The specific stagnation enthalpy of air in J/kg.
    """
    # Create a Solution object for air
    air = ct.Solution('air.yaml')

    # Set the temperature
    air.TP = t, 1 #the pressure value does not effect the enthalpy calculation( set it to a defualt 1)

    # Calculate the enthalpy
    h = air.enthalpy_mass
    # Total enthalpy or stagnation enthalpy v is velocity magnitude
    h_t = h + .5*v**2
    return h_t
def calculate_power(massdot, h4, h5):
    """
    Calculate power using the given equation.

    Parameters:
        massdot (float): Mass flow rate.
        h4 (float): Stagnation Enthalpy at state 4.
        h5 (float): Enthalpy at state 5.

    Returns:
        float: Calculated power.
    """
    return massdot * (h4 - h5)

def compressor_power(power_out_turbine, n_m=0.95):     #the efficiency paramater in the book is given as .95
    """
    Calculates the power delivered to the compressor based on the efficiency parameter
    and the power output of the turbine.

    Args:
    power_out_turbine (float): Power output of the turbine.
    n_m (float, optional): Efficiency parameter of the shaft. Defaults to 0.95.

    Returns:
    float: Power output to the compressor.
    """
    return n_m * power_out_turbine
