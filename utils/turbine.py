# turbine_model.py

class TurbineModel:
    """
    Class for modeling turbine behavior.
    """

    @staticmethod
    def calculate_total_enthalpy_out(ht_in, ht_out_ideal, eff):
        """
        Calculate the total enthalpy at the outlet of the turbine.

        Parameters:
        - ht_in (float): Total enthalpy at the inlet of the turbine.
        - ht_out_ideal (float): Ideal total enthalpy at the outlet of the turbine.
        - eff (float): Efficiency of the turbine.

        Returns:
        - float: Total enthalpy at the outlet of the turbine.
        """
        ht_out = ht_in + eff * (ht_in - ht_out_ideal)
        return ht_out
