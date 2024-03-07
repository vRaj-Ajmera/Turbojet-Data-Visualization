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
