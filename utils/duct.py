# duct_model.py

class DuctModel:
    """
    Class for modeling duct behavior.
    """

    @staticmethod
    def calculate_total_pressure_out(P_in, dP):
        """
        Calculate the total pressure at the outlet of the duct.

        Parameters:
        - P_in (float): Inlet pressure.
        - dP (float): Pressure loss term (typically less than 0.02).

        Returns:
        - float: Total pressure at the outlet of the duct.
        """
        Pt_out = (1 - dP) * P_in
        return Pt_out
