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

    # Calculating mass-flow parameter MFP
    def massFlowParameter(m_ci, A_i, p_ref, T_ref):
        numerator = m_ci * (T_ref**0.5)
        denominator = A_i * p_ref
        returm numerator/denominator

    # Corrected Engine Speed N_ci
    def corrEngineSpeed(N, theta_i):
        return N/(theta_i**0.5)

    # Corrected Thrust Fc
    def corrThrust(F, delta_0):
        return F/delta_0

    # Corrected Thrust specific fuel consumption S_c
    def corrTSFC(S, theta_0):
        return S/(theta_0**0.5)

    # Corrected fuel mass flow rate m_dot_fc
    def corrFMFR(m_dot_f, delta_2, theta_2)
        denominator = delta_2 * (theta_2**0.5)
        return m_dot_f / denominator

    # Specific m_dot_c2 calculation (gas generator)
    def calcMc2(T_4, T_2, pi_c, C_1):
        return C_1 * (pi_c / ((T_4/T_2)**0.5))
        
    # Turbine Characteristic: Capital Eta
    def capitalEta_i(gamma_i):
        return (gamma_i**0.5) * (2/(gamma_i + 1))**((gamma_i + 1)/(2*(gamma_i - 1)))

    # Corrected mass flow rate per unit area at station 4
    def calc_m4(p_4, A_4, gamma_i, T_4, R_4):
        numerator = p_4 * A_4 * capitalEta(gamma_i)
        denominator = (T_4**0.5) * (R_4**0.5)
        return numerator/denominator

    

    

