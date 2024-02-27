# nozzle_model.py

class NozzleModel:
    """
    Class for modeling nozzle behavior.
    """

    @staticmethod
    def calculate_thrust_guess(C_fg, W_in, V_out_ideal, g):
        """
        Calculate the thrust guess based on the provided parameters.

        Parameters:
        - C_fg (float): Coefficient of thrust.
        - W_in (float): Mass flow rate into the nozzle.
        - V_out_ideal (float): Ideal outlet velocity.
        - g (float): Acceleration due to gravity.

        Returns:
        - float: Thrust guess.
        """
        F_g = C_fg * (W_in * V_out_ideal) / g
        return F_g
