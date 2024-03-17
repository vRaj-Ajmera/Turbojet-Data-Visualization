# general_analysis.py

# The purpose of this file is to essentially draw out all the equations from Chapter 8 of the Mattingly textbook into one file.
# This is important because it does almost exactly what our project's goal was, to model engines based on certain inputs
# Seriously, read over Chapter 8 when you have the time, it explains what the inputs should be, what assumptions should be made,
# and how to combine them all together to gain graphs similar to 1-14a thru 1-14e in the Mattingly textbook

class GeneralAnalysis:

    # Calculating referece pressure ratio at any given station delta_i
    def pressureRef(p_ref, p)
        return p/p_ref

    # Calculating reference temperature ratio at any given station theta_i
    def temperatureRef(T_ref, T)
        return T/Tref

    # Calculating corrected mass flow rate m_dot_c at any station 'i'
    def corrMassFlowRate(m_dot_i, delta_i, theta_i):
        numerator = m_dot_i * (theta_i**0.5)
        return numerator / delta_i
