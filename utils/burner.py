# burner.py

class BurnerModel:
    """
    Class for modeling burner behavior.
    """

    @staticmethod
    def calculate_total_enthalpy_out(W_in_air, ht_in, W_fuel, LHV, eff, W_out):
        """
        Calculate the total enthalpy at the outlet of the burner.

        Parameters:
        - W_in_air (float): Mass flow rate of air (or oxidizer) into the burner.
        - ht_in (float): Total enthalpy at the inlet of the burner.
        - W_fuel (float): Mass flow rate of fuel into the burner.
        - LHV (float): Lower heating value of the fuel.
        - eff (float): Efficiency of the burner.
        - W_out (float): Mass flow rate at the outlet of the burner.

        Returns:
        - float: Total enthalpy at the outlet of the burner.
        """
        ht_out = (W_in_air * ht_in + W_fuel * LHV * eff) / W_out
        return ht_out
