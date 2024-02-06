# Sample utility functions for mathematical calculations

def calculate_thrust(throttle, efficiency):
    """
    Calculate thrust based on throttle setting and efficiency.

    Parameters:
    - throttle (float): Throttle setting (0.0 to 1.0).
    - efficiency (float): Efficiency factor.

    Returns:
    - float: Calculated thrust.
    """
    return throttle * efficiency * 1000  # Placeholder calculation, adjust as needed

def calculate_fuel_flow(power, efficiency):
    """
    Calculate fuel flow based on engine power and efficiency.

    Parameters:
    - power (float): Engine power.
    - efficiency (float): Efficiency factor.

    Returns:
    - float: Calculated fuel flow.
    """
    return power * efficiency * 0.013  # Placeholder calculation, adjust as needed
