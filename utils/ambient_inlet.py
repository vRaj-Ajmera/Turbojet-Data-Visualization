# ambient_inlet.py

class AmbientInletModel:
    """
    Class for modeling ambient and inlet conditions.
    """

    @staticmethod
    def calculate_drag(W_in, V_out, g):
        """
        Calculate drag force based on mass flow rate, outlet velocity, and gravity.

        Parameters:
        - W_in (float): Mass flow rate into the system.
        - V_out (float): Outlet velocity.
        - g (float): Acceleration due to gravity.

        Returns:
        - float: Calculated drag force.
        """
        drag_force = W_in * V_out / g
        return drag_force
